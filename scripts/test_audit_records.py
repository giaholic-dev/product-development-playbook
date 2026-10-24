"""Synthetic repository pages and optional Discussions traversal controls."""

import copy
import importlib.util
import json
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location('audit_records', Path(__file__).with_name('audit-records.py'))
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
REPO = 'fixture/repo'
TIME = '2026-10-23T12:00:00Z'


def response(payload, link=None):
    header = 'HTTP/2.0 200 OK\r\n'
    if link:
        header += 'Link: ' + link + '\r\n'
    return (header + '\r\n' + json.dumps(payload)).encode()


class Fixture:
    def __init__(self, repository=REPO, populated=True):
        self.repository = repository
        base = 'repos/' + repository
        self.routes = {base: response({'id': 1, 'full_name': repository}),
                       'user': response({'id': 2, 'login': 'reader', 'private_profile': 'not retained'})}
        for suffix in ('issues?state=all', 'pulls?state=all', 'labels?', 'milestones?state=all',
                       'releases?', 'issues/comments?'):
            sep = '&' if not suffix.endswith('?') else ''
            self.routes[base + '/' + suffix + sep + 'per_page=100&page=1'] = response([])
        self.issue = {'id': 10, 'node_id': 'CI1', 'number': 1, 'title': 'Work', 'body': 'Body',
                      'state': 'open', 'url': 'https://api.github.com/' + base + '/issues/1',
                      'labels': [], 'milestone': None}
        if populated:
            self.routes[base + '/issues?state=all&per_page=100&page=1'] = response([self.issue])
            self.routes[base + '/issues/1/timeline?per_page=100&page=1'] = response([
                {'event': 'referenced', 'commit_id': 'a', 'created_at': TIME},
                {'event': 'referenced', 'commit_id': 'b', 'created_at': TIME}])

    def __call__(self, target):
        if target not in self.routes:
            raise AssertionError('Unexpected fixture request: ' + target)
        result = self.routes[target]
        if isinstance(result, Exception):
            raise result
        return result


class RecordTests(unittest.TestCase):
    def setUp(self):
        self.fixture = Fixture()

    def collect(self, **kwargs):
        return R.collect(REPO, transport=self.fixture, **kwargs)

    def test_multipage_records_replay_and_idless_timeline(self):
        endpoint = 'repos/' + REPO + '/issues?state=all&per_page=100&page=1'
        next_endpoint = endpoint[:-1] + '2'
        self.fixture.routes[endpoint] = response([self.fixture.issue], '<https://api.github.com/' + next_endpoint + '>; rel="next"')
        self.fixture.routes[next_endpoint] = response([self.fixture.issue])
        out = self.collect()
        R.verify(out, REPO, False)
        self.assertEqual(len(out['issues.json']), 1)
        self.assertEqual(len(out['issue-timeline.json']), 2)
        self.assertEqual(out['records-requests.json'][1]['payload'], {'id': 2, 'login': 'reader'})
        self.assertEqual(out['records-coverage.json']['discussions']['status'], 'excluded')
        self.assertEqual(out['discussions.json'], [])

    def test_complete_empty_is_distinct_from_denial(self):
        out = R.collect(REPO, transport=Fixture(populated=False))
        R.verify(out, REPO, False)
        self.assertEqual(out['issues.json'], [])
        self.fixture.routes['repos/' + REPO + '/labels?per_page=100&page=1'] = R.PR.EvidenceError('denied')
        with self.assertRaises(R.PR.EvidenceError):
            self.collect()

    def test_page_and_after_cursor_preserved_and_replayed(self):
        first = 'repos/' + REPO + '/issues?state=all&per_page=100&page=1'
        second = 'repositories/1/issues?state=all&per_page=100&page=2&after=opaque%2Bcursor%3D'
        third = 'repositories/1/issues?state=all&per_page=100&page=3&after=next%3D'
        self.fixture.routes[first] = response([self.fixture.issue], '<https://api.github.com/' + second + '>; rel="next"')
        self.fixture.routes[second] = response([], '<https://api.github.com/' + third + '>; rel="next"')
        self.fixture.routes[third] = response([])
        out = self.collect()
        R.verify(out, REPO, False)
        observation = out['records-coverage.json']['observations'][0]
        self.assertEqual([p['request'] for p in observation['pages']], [first, second, third])
        self.assertEqual(len(out['issues.json']), 1)

    def test_cursor_does_not_allow_changed_scope_or_parameters(self):
        first = 'repos/' + REPO + '/issues?state=all&per_page=100&page=1'
        prefix = 'https://api.github.com/repositories/1/issues?'
        for query in ('state=closed&per_page=100&page=2&after=a',
                      'state=all&per_page=50&page=2&after=a',
                      'state=all&per_page=100&page=1&after=a',
                      'state=all&per_page=100&page=3&after=a',
                      'state=all&per_page=100&page=2&after=',
                      'state=all&per_page=100&page=2&after=a&after=b',
                      'state=all&per_page=100&page=2&after=a&before=b',
                      'state=all&per_page=100&page=2&after=a&unexpected=b',
                      'state=all&per_page=100&after=a'):
            with self.subTest(query=query):
                self.fixture.routes[first] = response([], '<' + prefix + query + '>; rel="next"')
                with self.assertRaises(R.P.ProjectError):
                    self.collect()
        for url in ('https://evil.example/repositories/1/issues',
                    'https://api.github.com/repositories/2/issues',
                    'https://api.github.com/repositories/1/pulls'):
            self.fixture.routes[first] = response([], '<' + url + '?state=all&per_page=100&page=2&after=a>; rel="next"')
            with self.assertRaises(R.P.ProjectError):
                self.collect()

    def test_repeated_or_disappearing_cursor_fails(self):
        first = 'repos/' + REPO + '/issues?state=all&per_page=100&page=1'
        second = 'repositories/1/issues?state=all&per_page=100&page=2&after=a'
        third = 'repositories/1/issues?state=all&per_page=100&page=3&after=b'
        self.fixture.routes[first] = response([], '<https://api.github.com/' + second + '>; rel="next"')
        self.fixture.routes[second] = response([], '<https://api.github.com/' + third + '>; rel="next"')
        for suffix in ('&after=b', '&after=a', ''):
            fourth = 'repositories/1/issues?state=all&per_page=100&page=4' + suffix
            self.fixture.routes[third] = response([], '<https://api.github.com/' + fourth + '>; rel="next"')
            with self.subTest(suffix=suffix), self.assertRaises(R.P.ProjectError):
                self.collect()

    def test_foreign_or_conflicting_records_fail(self):
        for variant in ('foreign', 'conflict', 'missing'):
            with self.subTest(variant=variant):
                self.fixture = Fixture()
                record = copy.deepcopy(self.fixture.issue)
                if variant == 'foreign':
                    record['url'] = 'https://api.github.com/repos/other/repo/issues/1'
                elif variant == 'conflict':
                    record['title'] = 'changed'
                else:
                    record.pop('id')
                self.fixture.routes['repos/' + REPO + '/issues?state=all&per_page=100&page=1'] = response([self.fixture.issue, record])
                with self.assertRaises(R.P.ProjectError):
                    self.collect()

    def test_bad_next_links_fail(self):
        endpoint = 'repos/' + REPO + '/labels?per_page=100&page=1'
        for link in ('https://evil.example/labels?page=2',
                     'https://api.github.com/repos/other/repo/labels?per_page=100&page=2',
                     'https://api.github.com/repos/fixture/repo/labels?per_page=100&page=1',
                     'https://api.github.com/repos/fixture/repo/labels?per_page=100&page=3'):
            with self.subTest(link=link):
                self.fixture.routes[endpoint] = response([], '<' + link + '>; rel="next"')
                with self.assertRaises(R.P.ProjectError):
                    self.collect()

    def test_conflicting_timeline_identity_and_missing_parent_fail(self):
        endpoint = 'repos/' + REPO + '/issues/1/timeline?per_page=100&page=1'
        self.fixture.routes[endpoint] = response([{'id': 1, 'event': 'labeled', 'label': 'a'},
                                                  {'id': 1, 'event': 'labeled', 'label': 'b'}])
        with self.assertRaises(R.P.ProjectError):
            self.collect()
        self.fixture = Fixture()
        endpoint = 'repos/' + REPO + '/issues/comments?per_page=100&page=1'
        self.fixture.routes[endpoint] = response([{'id': 40, 'issue_url': 'https://api.github.com/repos/' + REPO + '/issues/999'}])
        with self.assertRaises(R.P.ProjectError):
            self.collect()

    def test_optional_discussions_pages_and_partial_errors(self):
        def graphql(query, variables):
            cursor = variables['cursor']
            number = 1 if cursor is None else 2
            return {'data': {'repository': {'nameWithOwner': REPO, 'discussions': {
                'nodes': [{'id': 'D' + str(number), 'number': number, 'title': 'Discussion', 'body': 'Body',
                           'createdAt': TIME, 'updatedAt': TIME, 'url': 'https://github.com/fixture/repo/discussions/' + str(number)}],
                'totalCount': 2, 'pageInfo': {'hasNextPage': number == 1, 'endCursor': str(number)}}}}}
        out = self.collect(discussions=True, graphql=graphql)
        R.verify(out, REPO, True)
        self.assertEqual(len(out['discussions.json']), 2)
        with self.assertRaises(R.P.ProjectError):
            self.collect(discussions=True, graphql=lambda q, v: {'data': {}, 'errors': [{'message': 'denied'}]})

    def test_offline_corruption_is_rejected(self):
        original = self.collect()
        for mutate in (lambda out: out['issues.json'].clear(),
                       lambda out: out['records-requests.json'].pop(),
                       lambda out: out['records-coverage.json']['observations'].pop(),
                       lambda out: out['records-coverage.json']['discussions'].update(status='complete')):
            with self.subTest(mutate=mutate):
                out = copy.deepcopy(original)
                mutate(out)
                with self.assertRaises(R.P.ProjectError):
                    R.verify(out, REPO, False)


if __name__ == '__main__':
    unittest.main()
