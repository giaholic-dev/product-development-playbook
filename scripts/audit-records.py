#!/usr/bin/env python3
"""Read-only repository records with retained page evidence and offline replay."""

import argparse
import copy
import importlib.util
import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlsplit


def helper(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), Path(__file__).with_name(name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


P = helper('audit-project')
PR = helper('audit-pr-evidence')
FILES = {
    'issues': 'issues.json', 'pull_requests': 'pull-requests.json',
    'issue_comments': 'issue-comments.json', 'issue_timeline': 'issue-timeline.json',
    'labels': 'labels.json', 'milestones': 'milestones.json', 'releases': 'releases.json',
}
OUTPUTS = tuple(FILES.values()) + ('records-coverage.json', 'records-requests.json', 'discussions.json')


class Client:
    def __init__(self, repository, transport=PR.gh_get):
        P.require(re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository), 'Invalid repository target.')
        self.repository, self.transport = repository, transport
        self.requests, self.observations = [], []
        self.started_at = P.now()
        self.repository_record = self.read('repos/' + repository)
        P.require(isinstance(self.repository_record, dict) and PR.positive_id(self.repository_record.get('id'))
                  and self.repository_record.get('full_name', '').casefold() == repository.casefold(),
                  'Repository identity inaccessible/mismatched.')
        raw_principal = self.read('user')
        P.require(isinstance(raw_principal, dict) and PR.positive_id(raw_principal.get('id'))
                  and isinstance(raw_principal.get('login'), str), 'Missing observed principal.')
        self.principal = {k: raw_principal[k] for k in ('id', 'login')}
        # Retain only the needed principal identity, never the user's full profile.
        self.requests[-1]['payload'] = self.principal

    def read(self, endpoint):
        headers, payload = PR.parse_response(self.transport(endpoint))
        allowed_headers = {k: headers[k] for k in ('link', 'x-github-request-id') if k in headers}
        self.requests.append({'endpoint': endpoint, 'headers': allowed_headers, 'payload': copy.deepcopy(payload)})
        return payload

    def target(self, url, suffix):
        parsed = urlsplit(url)
        P.require(parsed.scheme == 'https' and parsed.netloc == 'api.github.com' and not parsed.fragment,
                  'Unsafe repository reference.')
        allowed = {'/repos/' + self.repository + '/' + suffix,
                   '/repositories/' + str(self.repository_record['id']) + '/' + suffix}
        P.require(parsed.path.casefold() in {p.casefold() for p in allowed}, 'Reference escapes selected repository.')
        return parsed

    def collect(self, suffix, params, target, key):
        started, page, records, pages, seen = P.now(), 1, {}, [], set()
        cursors = set()
        endpoint = 'repos/' + self.repository + '/' + suffix + '?' + urlencode(dict(params, per_page=100, page=page))
        for _ in range(10000):
            P.require(endpoint not in seen, 'Repeated repository page request.')
            seen.add(endpoint)
            payload = self.read(endpoint)
            headers = self.requests[-1]['headers']
            P.require(isinstance(payload, list), 'Required repository collection is not an array.')
            for record in payload:
                P.require(isinstance(record, dict), 'Invalid repository record.')
                identity = key(record)
                P.require(identity not in records or records[identity] == record,
                          'Conflicting duplicate repository record.')
                records[identity] = record
            link = headers.get('link', '')
            links = re.findall(r'<([^>]+)>\s*;\s*rel="([^"]+)"', link)
            P.require(not link or (links and len(links) == len(link.split(','))), 'Invalid pagination header.')
            next_links = [url for url, relation in links if relation == 'next']
            P.require(len(next_links) <= 1, 'Ambiguous page continuation.')
            next_endpoint = None
            if next_links:
                parsed = self.target(next_links[0], suffix)
                expected = {k: [str(v)] for k, v in dict(params, per_page=100, page=page + 1).items()}
                query = parse_qs(parsed.query, keep_blank_values=True)
                # GitHub may return page + an opaque after cursor. Preserve the
                # provider link, but never permit changed filters or cursor loops.
                after = query.pop('after', None)
                P.require(query == expected, 'Nonadvancing/changed page parameters.')
                if after is not None:
                    P.require(len(after) == 1 and bool(after[0]) and after[0] not in cursors,
                              'Invalid/repeated repository page cursor.')
                    cursors.add(after[0])
                else:
                    P.require(not cursors, 'Repository page cursor disappeared.')
                next_endpoint = parsed.path.lstrip('/') + '?' + parsed.query
            pages.append({'request': endpoint, 'next': next_endpoint, 'status': 200,
                          'returned_count': len(payload), 'observed_at': P.now()})
            if next_endpoint is None:
                break
            endpoint, page = next_endpoint, page + 1
        else:
            raise P.ProjectError('Repository page resource limit reached.')
        self.observations.append({'target': target, 'status': 'complete', 'started_at': started,
                                  'ended_at': P.now(), 'pages': pages, 'terminal_no_next': True,
                                  'raw_count': sum(p['returned_count'] for p in pages), 'retained_count': len(records)})
        return list(records.values())


def record_id(record):
    P.require(PR.positive_id(record.get('id')), 'Missing repository provider identity.')
    return record['id']


def timeline_key(record):
    P.require(isinstance(record.get('event'), str), 'Missing timeline event kind.')
    if record.get('id') is not None:
        return (record['event'], record_id(record))
    return ('payload', json.dumps(record, sort_keys=True, ensure_ascii=True, allow_nan=False))


def collect(repository, discussions=False, transport=PR.gh_get, graphql=P.gh_query):
    client = Client(repository, transport)
    outputs = {}
    for name, suffix, params in (
        ('issues', 'issues', {'state': 'all'}), ('pull_requests', 'pulls', {'state': 'all'}),
        ('labels', 'labels', {}), ('milestones', 'milestones', {'state': 'all'}),
        ('releases', 'releases', {}), ('issue_comments', 'issues/comments', {}),
    ):
        outputs[name] = client.collect(suffix, params, [name], record_id)
    outputs['issues'] = [r for r in outputs['issues'] if 'pull_request' not in r]
    for name in ('issues', 'pull_requests'):
        numbers = set()
        for record in outputs[name]:
            number = record.get('number')
            P.require(PR.positive_id(number) and number not in numbers, 'Invalid/duplicate work-item number.')
            numbers.add(number)
            client.target(record.get('url', ''), ('issues/' if name == 'issues' else 'pulls/') + str(number))
            P.require(isinstance(record.get('title'), str) and 'body' in record and isinstance(record.get('state'), str),
                      'Incomplete work-item metadata.')
    issues = {r['number']: r for r in outputs['issues']}
    prs = {r['number']: r for r in outputs['pull_requests']}
    P.require(not set(issues) & set(prs), 'Issue/PR number overlap.')
    comments = []
    for record in outputs['issue_comments']:
        parent = record.get('issue_url', '')
        number_text = urlsplit(parent).path.rsplit('/', 1)[-1]
        P.require(number_text.isdigit(), 'Invalid comment parent.')
        number = int(number_text)
        client.target(parent, 'issues/' + str(number))
        P.require(number in issues or number in prs, 'Comment parent absent from observed repository.')
        P.require(isinstance(record.get('body'), str), 'Missing comment body.')
        if number in issues:
            comments.append(dict(record, issue_number=number))
    outputs['issue_comments'] = comments
    timelines = []
    for number in sorted(issues):
        records = client.collect('issues/' + str(number) + '/timeline', {}, ['issue_timeline', number], timeline_key)
        timelines.extend(dict(r, issue_number=number) for r in records)
    outputs['issue_timeline'] = timelines
    for name, records in outputs.items():
        records.sort(key=lambda r: (r.get('number', r.get('issue_number', 0)), str(r.get('id', '')), json.dumps(r, sort_keys=True)))
    discussion_records, discussion_observations, discussion_requests = [], [], []
    if discussions:
        graph = P.Client(graphql)
        query = '''query($owner:String!,$repository:String!,$cursor:String){repository(owner:$owner,name:$repository){
nameWithOwner discussions(first:100,after:$cursor){nodes{id number title body createdAt updatedAt url category{id name} author{login}}
pageInfo{hasNextPage endCursor} totalCount}}}'''
        def resolve(data):
            repo = data.get('repository')
            P.require(isinstance(repo, dict) and repo.get('nameWithOwner', '').casefold() == repository.casefold(),
                      'Discussion repository inaccessible/mismatched.')
            return repo.get('discussions')
        owner, name = repository.split('/')
        discussion_records = graph.traverse(query, {'owner': owner, 'repository': name}, resolve,
                                            lambda r: r.get('id'), ['discussions'])
        for record in discussion_records:
            P.require(PR.positive_id(record.get('number'))
                      and all(isinstance(record.get(k), str) for k in ('title', 'body', 'createdAt', 'updatedAt', 'url')),
                      'Incomplete Discussion metadata.')
        discussion_observations, discussion_requests = graph.observations, graph.requests
    coverage = {'evidence_schema_version': '1.0.0', 'api_version': PR.API_VERSION,
                'repository': repository, 'repository_id': client.repository_record['id'], 'principal': client.principal,
                'started_at': client.started_at, 'ended_at': P.now(), 'observations': client.observations,
                'discussions': {'selected': discussions, 'status': 'complete' if discussions else 'excluded',
                                'reason': None if discussions else 'Optional Discussions not selected before collection.',
                                'observations': discussion_observations, 'requests': discussion_requests},
                'counts': {name: len(records) for name, records in outputs.items()}}
    files = {FILES[name]: records for name, records in outputs.items()}
    files.update({'records-coverage.json': coverage, 'records-requests.json': client.requests,
                  'discussions.json': discussion_records})
    return files


def untimed(value):
    if isinstance(value, dict):
        return {k: untimed(v) for k, v in value.items() if k not in {'started_at', 'ended_at', 'observed_at'}}
    if isinstance(value, list):
        return [untimed(v) for v in value]
    return value


def verify(outputs, repository, discussions):
    P.require(set(outputs) == set(OUTPUTS), 'Missing repository evidence payload.')
    requests = iter(outputs['records-requests.json'])
    graph_requests = iter(outputs['records-coverage.json']['discussions']['requests'])
    def replay(endpoint):
        record = next(requests, None)
        P.require(isinstance(record, dict) and record.get('endpoint') == endpoint, 'Missing/changed repository request.')
        headers = record['headers']
        P.require(set(headers) <= {'link', 'x-github-request-id'}, 'Unexpected retained request metadata.')
        encoded_headers = 'HTTP/2.0 200 OK\r\n' + ''.join(k + ': ' + v + '\r\n' for k, v in headers.items())
        return (encoded_headers + '\r\n' + json.dumps(record['payload'], allow_nan=False)).encode()
    def graph_replay(query, variables):
        record = next(graph_requests, None)
        P.require(isinstance(record, dict) and record.get('query_sha256') == P.fingerprint(query)
                  and record.get('variables') == variables, 'Missing/changed Discussions request.')
        return record['response']
    expected = collect(repository, discussions, replay, graph_replay)
    P.require(next(requests, None) is None and next(graph_requests, None) is None, 'Unexpected extra repository request.')
    P.require(untimed(outputs) == untimed(expected), 'Repository output differs from retained response evidence.')
    return outputs['records-coverage.json']


def write(outputs, destination):
    destination = Path(destination)
    P.require(not any((destination / n).exists() or (destination / n).is_symlink() for n in OUTPUTS),
              'Refusing to overwrite repository evidence.')
    destination.mkdir(parents=True, exist_ok=True, mode=0o700)
    for name, value in outputs.items():
        with (destination / name).open('x', encoding='utf-8') as stream:
            os.chmod(stream.name, 0o600)
            json.dump(value, stream, indent=2, ensure_ascii=True, allow_nan=False)
            stream.write('\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('collect', 'verify'))
    parser.add_argument('--repository', required=True)
    parser.add_argument('--discussions', choices=('true', 'false'), default='false')
    parser.add_argument('--destination', required=True, type=Path)
    args = parser.parse_args()
    try:
        selected = args.discussions == 'true'
        if args.action == 'collect':
            outputs = collect(args.repository, selected)
            verify(outputs, args.repository, selected)
            write(outputs, args.destination)
        else:
            outputs = {n: P.json_load((args.destination / n).read_bytes()) for n in OUTPUTS}
            verify(outputs, args.repository, selected)
    except (P.ProjectError, PR.EvidenceError, OSError, TypeError, ValueError, KeyError, AttributeError):
        print('ERROR: Required repository records incomplete/invalid; no complete package.', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
