#!/usr/bin/env python3
"""Seal, verify and safely finalize schema-2 offline audit packages."""

import argparse
import hashlib
import json
import os
import shutil
import stat
import sys
import tempfile
import zipfile
from datetime import datetime
from pathlib import Path

import importlib.util


def helper(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), Path(__file__).with_name(name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


P = helper('audit-project')
R = helper('audit-records')
PR = helper('audit-pr-evidence')
S = helper('audit-source')
VERSION = '2.0.0'
CONTRACT = 'audit-package-coverage/2.0.0'
SUPPORTED_TOOLS = {'2.0.0', '2.0.1'}


def read(root, name):
    return P.json_load((root / name).read_bytes())


def inventory(root):
    root = Path(root)
    P.require(root.is_dir() and not root.is_symlink(), 'Unsafe package root.')
    records, folded = [], set()
    for path in sorted(root.rglob('*')):
        P.require(not path.is_symlink(), 'Package payload symlinks are forbidden.')
        name = path.relative_to(root).as_posix()
        S.safe_path(name)
        P.require(name.casefold() not in folded, 'Case-colliding package paths.')
        folded.add(name.casefold())
        if path.is_dir():
            continue
        P.require(stat.S_ISREG(path.stat().st_mode), 'Nonregular package payload.')
        if name == 'manifest.json':
            continue
        data = path.read_bytes()
        records.append({'path': name, 'size_bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
    return records


def check_source(root):
    source = read(root, 'repository/source-inventory.json')
    P.require(source.get('snapshot_schema_version') == '1.0.0' and source.get('policy_version') == S.POLICY_VERSION
              and source.get('policy') == S.source_policy() and source.get('source_kind') == 'committed-git-tree'
              and source.get('working_tree_bytes_included') is False, 'Unsupported source policy/byte claim.')
    P.require(all(isinstance(source.get(k), bool) for k in ('dirty_initial', 'dirty_final', 'all_tracked_blobs_retained')),
              'Invalid source state types.')
    commit, tree = source.get('commit'), source.get('tree')
    P.require(isinstance(commit, str) and len(commit) in (40, 64) and isinstance(tree, str)
              and len(tree) == len(commit) and all(c in '0123456789abcdef' for c in commit + tree),
              'Invalid declared source identity.')
    algorithm = hashlib.sha1 if len(commit) == 40 else hashlib.sha256
    entries = source.get('entries')
    P.require(isinstance(entries, list) and source.get('tracked_entries') == len(entries), 'Source entry count mismatch.')
    paths, expected, directories = set(), set(), {}
    for record in entries:
        name = record['path']
        parts = S.safe_path(name).parts
        P.require(name.casefold() not in paths, 'Duplicate source inventory path.')
        paths.add(name.casefold())
        oid, mode = record.get('object_id'), record.get('mode')
        P.require(isinstance(oid, str) and len(oid) == len(commit)
                  and all(c in '0123456789abcdef' for c in oid), 'Invalid source object identity.')
        P.require((mode, record.get('git_type')) in {('100644', 'blob'), ('100755', 'blob'),
                                                              ('120000', 'blob'), ('160000', 'commit')},
                  'Invalid source mode/type.')
        disposition = record.get('disposition')
        P.require(disposition in {'retained', 'excluded', 'gitlink-only', 'lfs-pointer-only'}, 'Unknown source disposition.')
        if S.required_source(name):
            P.require(disposition == 'retained', 'Required audit source is not retained.')
        reason = S.exclusion(name, source['output_relative'])
        if reason:
            P.require(disposition == 'excluded' and record.get('reason') == reason
                      and 'sha256' not in record, 'Protected source exclusion mismatch.')
        else:
            P.require(disposition != 'excluded', 'Unapproved source exclusion.')
        if 'sha256' in record:
            expected.add(name)
            data = (root / 'repository/source' / name).read_bytes()
            P.require(len(data) == record['size_bytes'] and hashlib.sha256(data).hexdigest() == record['sha256'],
                      'Source hash/size mismatch.')
            object_id = algorithm(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
            P.require(object_id == oid, 'Source bytes differ from declared Git blob.')
            P.require((disposition == 'lfs-pointer-only') == data.startswith(b'version https://git-lfs.github.com/spec/v1\n'),
                      'Git LFS pointer disposition mismatch.')
        else:
            P.require(disposition in {'excluded', 'gitlink-only'}, 'Missing source payload/hash.')
        current = directories
        for part in parts[:-1]:
            current = current.setdefault(part, {})
            P.require(isinstance(current, dict), 'Source file/directory collision.')
        P.require(parts[-1] not in current, 'Duplicate source leaf.')
        current[parts[-1]] = (mode, oid)
    P.require('readme.md' in paths, 'Missing required source README.')
    actual = {p.relative_to(root / 'repository/source').as_posix()
              for p in (root / 'repository/source').rglob('*') if p.is_file()}
    P.require(actual == expected, 'Unexpected/missing source payload.')
    def git_tree(directory):
        records = []
        for name, node in directory.items():
            if isinstance(node, dict):
                mode, oid = '40000', git_tree(node)
                sort_key = name.encode() + b'/'
            else:
                mode, oid = node
                sort_key = name.encode()
            records.append((sort_key, mode.encode() + b' ' + name.encode() + b'\0' + bytes.fromhex(oid)))
        data = b''.join(record for _, record in sorted(records))
        return algorithm(b'tree ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    P.require(git_tree(directories) == tree, 'Inventory does not reconstruct the declared Git tree.')
    P.require(source['all_tracked_blobs_retained'] == all(r['disposition'] == 'retained' for r in entries),
              'Source completeness summary mismatch.')
    # Legacy convenience copies must also come from the declared retained source.
    P.require((root / 'repository/README.md').read_bytes() == (root / 'repository/source/README.md').read_bytes(),
              'Legacy README differs from committed source.')
    for directory in ('docs', 'templates', 'examples'):
        original = root / 'repository/source' / directory
        for path in original.rglob('*'):
            if path.is_file():
                P.require((root / 'repository' / directory / path.relative_to(original)).read_bytes() == path.read_bytes(),
                          'Legacy document differs from declared source.')
    return source


def validate_interval(coverage):
    start, end = datetime.fromisoformat(coverage['started_at']), datetime.fromisoformat(coverage['ended_at'])
    P.require(start.tzinfo is not None and end.tzinfo is not None and start <= end, 'Invalid observation interval.')
    for observation in coverage.get('observations', []):
        observed_start = datetime.fromisoformat(observation['started_at'])
        observed_end = datetime.fromisoformat(observation['ended_at'])
        P.require(start <= observed_start <= observed_end <= end, 'Collection interval escapes run interval.')
        for page in observation.get('pages', []):
            timestamp = datetime.fromisoformat(page['observed_at'])
            P.require(observed_start <= timestamp <= observed_end, 'Page interval escapes collection.')
    return {'started_at': coverage['started_at'], 'ended_at': coverage['ended_at']}


def derive(root, base):
    root = Path(root)
    # Reject unknown/legacy versions rather than validating them as full coverage.
    P.require(base.get('schema_version') == VERSION and base.get('tool_version') in SUPPORTED_TOOLS,
              'Full validation requires schema 2.0.0 and a supported tool 2.0.x; legacy packages need a new authorized export.')
    repository = base['repository']['owner'] + '/' + base['repository']['name']
    P.require(R.re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository), 'Invalid manifest repository name.')
    repo_meta = base['repository']
    P.require(isinstance(repo_meta.get('dirty'), bool) and isinstance(repo_meta.get('detached_head'), bool)
              and isinstance(repo_meta.get('selected_ref'), str) and repo_meta['selected_ref']
              and all(repo_meta.get(k) is None or isinstance(repo_meta.get(k), str) for k in ('branch', 'default_branch')),
              'Invalid manifest repository metadata types.')
    P.require(not repo_meta['detached_head'] or (repo_meta.get('branch') is None
              and repo_meta['selected_ref'] == repo_meta['commit']), 'Detached source ref mismatch.')
    generated = datetime.fromisoformat(base['generated_at'])
    P.require(generated.tzinfo is not None, 'Manifest generation time lacks timezone.')
    P.require(all(isinstance(v, int) and not isinstance(v, bool) and v >= 0 for v in base['collection_counts'].values())
              and all(v is True for v in base['collection_pagination'].values()), 'Invalid compatibility count/pagination types.')
    P.require(base['repository']['remote_identity'] == 'github.com/' + repository, 'Repository identity mismatch.')
    payloads = inventory(root)  # Reject unsafe filesystem entries before any JSON/payload reads.
    source = check_source(root)
    P.require(source['commit'] == base['repository']['commit'], 'Manifest/source commit mismatch.')
    summary = base['source_snapshot']
    for key in ('commit', 'tree', 'source_kind', 'working_tree_bytes_included', 'all_tracked_blobs_retained',
                'policy_version', 'dirty_initial', 'dirty_final'):
        P.require(summary.get(key) == source[key], 'Source summary contradicts inventory.')
    P.require(summary.get('inventory') == 'repository/source-inventory.json'
              and summary.get('root') == 'repository/source', 'Source path summary mismatch.')
    records = {name: read(root, 'github/' + name) for name in R.OUTPUTS}
    selected_discussions = records['records-coverage.json']['discussions']['selected']
    P.require(isinstance(selected_discussions, bool), 'Unknown Discussions selection.')
    records_coverage = R.verify(records, repository, selected_discussions)
    validate_interval(records_coverage)
    project = {name: read(root, 'github/' + name) for name in P.OUTPUTS}
    project_identity = project['project-coverage.json']['project']
    P.verify(project, project_identity['owner_kind'], project_identity['owner_login'], project_identity['number'], repository)
    project_coverage = project['project-coverage.json']
    P.require(base['project_evidence']['project'] == project_identity, 'Selected Project identity mismatch.')
    P.require(project_coverage['principal']['login'].casefold() == records_coverage['principal']['login'].casefold(),
              'Required collectors used different observed principals.')
    prs = records['pull-requests.json']
    pr_coverage = PR.verify_evidence(repository, prs, root / 'github')
    P.require(pr_coverage['repository_id'] == records_coverage['repository_id']
              and pr_coverage['scope'] == 'authorized-observable-pr-evidence', 'PR/repository scope mismatch.')
    P.require(pr_coverage['principal'] == records_coverage['principal'], 'Repository/PR principal identity mismatch.')
    P.require(base['pr_evidence'] == {'coverage': 'github/pr-evidence-coverage.json',
              'evidence_schema_version': pr_coverage['evidence_schema_version'], 'scope': pr_coverage['scope'],
              'current_approval_inferred': False}, 'PR summary contradicts coverage.')
    P.require(base['project_evidence'] == {'coverage': 'github/project-coverage.json',
              'transcript': 'github/project-requests.json', 'values': 'github/project-values.json',
              'evidence_schema_version': project_coverage['evidence_schema_version'],
              'project': project_identity, 'scope': project_coverage['scope']}, 'Project summary contradicts coverage.')
    # Cross-collector local issue/PR references; foreign references remain explicitly external.
    issues = {i['number']: i for i in records['issues.json']}
    pulls = {p['number']: p for p in prs}
    conversations = read(root, 'github/pr-conversations.json')
    shared_comments = {}
    for request in records['records-requests.json']:
        if request['endpoint'].split('?')[0].endswith('/issues/comments'):
            for comment in request['payload']:
                number = int(comment['issue_url'].rsplit('/', 1)[-1])
                if number in pulls:
                    shared_comments[comment['id']] = comment
    P.require(shared_comments == {c['id']: {k: v for k, v in c.items() if k != 'pull_request_number'} for c in conversations},
              'Repository/PR conversation observations changed; retry as a new run.')
    labels = {l['id'] for l in records['labels.json']}
    milestones = {m['id'] for m in records['milestones.json']}
    for item in list(issues.values()) + list(pulls.values()):
        for label in item.get('labels', []):
            P.require(label.get('id') in labels, 'Work item references missing label.')
        if item.get('milestone') is not None:
            P.require(item['milestone'].get('id') in milestones, 'Work item references missing milestone.')
    for item in project['project-items.json']:
        if item['content_disposition'] == 'local':
            content = item['content']
            work = (issues if item['type'] == 'ISSUE' else pulls).get(content.get('number'))
            P.require(work is not None and work.get('node_id') == content.get('id'),
                      'Local Project content does not join observed repository work.')
    for name in ('branches.txt', 'tags.txt', 'recent-commits.tsv', 'status.txt'):
        P.require((root / 'git' / name).is_file(), 'Missing required local Git evidence.')
    P.require(len((root / 'git/recent-commits.tsv').read_bytes().splitlines()) <= 100,
              'Local history exceeds declared limit.')
    allowed = {'git/' + n for n in ('branches.txt', 'tags.txt', 'recent-commits.tsv', 'status.txt')}
    allowed |= {'github/' + n for n in set(R.OUTPUTS) | set(P.OUTPUTS) | set(PR.FILES.values()) | {'pr-evidence-coverage.json'}}
    allowed |= {'repository/source-inventory.json', 'repository/README.md', 'repository/repository-tree.txt'}
    for record in source['entries']:
        if 'sha256' not in record:
            continue
        name = record['path']
        allowed.add('repository/source/' + name)
        if name.split('/')[0] in {'docs', 'templates', 'examples'}:
            allowed.add('repository/' + name)
        if name in {'.editorconfig', '.gitignore', '.shellcheckrc', '.gitattributes', 'CODEOWNERS', 'Makefile'}:
            allowed.add('repository/config/' + name)
            P.require((root / ('repository/config/' + name)).read_bytes()
                      == (root / ('repository/source/' + name)).read_bytes(), 'Legacy config/source mismatch.')
    P.require({p['path'] for p in payloads} == allowed, 'Missing required or unexpected package payload.')
    convenience = [json.loads(line) for line in (root / 'repository/repository-tree.txt').read_text().splitlines()]
    P.require(convenience == [r['path'] for r in source['entries']], 'Source path convenience index mismatch.')
    collections = []
    def add(name, path, count, evidence, required=True, status='complete', reason=None):
        collections.append({'name': name, 'path': path, 'required': required, 'status': status,
                            'retained_count': count, 'evidence': evidence, 'reason': reason})
    record_observations = records_coverage['observations']
    for name, filename in R.FILES.items():
        obs = [o for o in record_observations if o['target'][0] == name]
        add(name, 'github/' + filename, len(records[filename]), {'observations': obs,
            'raw_count': sum(o['raw_count'] for o in obs), 'interval': validate_interval(records_coverage)})
    for name, filename, kind in (('pr_conversations', 'pr-conversations.json', 'conversations'),
                                 ('pr_reviews', 'pr-reviews.json', 'reviews'),
                                 ('review_comments', 'review-comments.json', 'inline_comments')):
        observations = [o for o in pr_coverage['observations'] if o['kind'] == kind]
        add(name, 'github/' + filename, len(read(root, 'github/' + filename)),
            {'observations': observations, 'raw_count': sum(o['raw_count'] for o in observations)})
    for name, filename, target in (('project_items', 'project-items.json', 'items'),
                                   ('project_fields', 'project-fields.json', 'fields'),
                                   ('project_views', 'project-views.json', 'views'),
                                   ('project_values', 'project-values.json', 'values')):
        obs = [o for o in project_coverage['observations'] if o['target'][0] == target]
        add(name, 'github/' + filename, len(project[filename]), {'observations': obs,
            'raw_count': sum(o['raw_count'] for o in obs), 'interval': validate_interval(project_coverage)})
    discussion = records_coverage['discussions']
    add('discussions', 'github/discussions.json', len(records['discussions.json']), discussion,
        required=selected_discussions, status=discussion['status'], reason=discussion['reason'])
    add('source', 'repository/source-inventory.json', len(source['entries']),
        {'commit': source['commit'], 'tree': source['tree'], 'policy': source['policy'],
         'policy_version': source['policy_version'], 'dispositions': source['entries']})
    for name in ('branches', 'tags', 'recent-commits', 'status'):
        path = 'git/' + name + ('.tsv' if name == 'recent-commits' else '.txt')
        add('local_' + name, path, len((root / path).read_bytes().splitlines()),
            {'scope': 'local-only', 'history_limit': 100 if name == 'recent-commits' else None,
             'remote_freshness_claimed': False})
    counts = {c['name']: c['retained_count'] for c in collections if c['name'] in base['collection_counts']}
    P.require(counts == base['collection_counts'], 'Legacy collection counts contradict verified evidence.')
    pagination = {name: True for name in counts}
    P.require(base['collection_pagination'] == pagination, 'Legacy pagination summary contradicts evidence.')
    complete = all(c['status'] == 'complete' for c in collections if c['required'])
    complete = complete and all(c['status'] in {'complete', 'excluded'} for c in collections)
    result = {k: base[k] for k in ('schema_version', 'tool_version', 'repository', 'generated_at',
                                   'source_snapshot', 'project_evidence', 'pr_evidence',
                                   'collection_counts', 'collection_pagination')}
    result.update(contract=CONTRACT, coverage_profile='authorized-observable-full',
                  full_profile_complete=complete, project=project_identity, source_tree=source['tree'],
                  collections=collections, payload_inventory=payloads,
                  observation={'repository': validate_interval(records_coverage),
                               'project': validate_interval(project_coverage),
                               'source_started_at': source['observation_started_at'],
                               'source_ended_at': source['observation_ended_at'],
                               'pr_identity_observed_at': pr_coverage['identity_observed_at'],
                               'atomic_provider_snapshot': False},
                  principal=records_coverage['principal'],
                  integrity={'source_tree_reconstructed': True, 'source_blobs_verified': True,
                             'pr_relations_verified': True, 'project_replay_verified': True,
                             'repository_replay_verified': True, 'local_references_verified': True,
                             'payload_hashes_verified': True, 'manifest_self_hash_excluded': True})
    P.require(complete, 'Required coverage is incomplete.')
    return result


def seal(root):
    root = Path(root)
    base = read(root, 'manifest.json')
    manifest = derive(root, base)
    path = root / 'manifest.json'
    with path.open('w', encoding='utf-8') as stream:
        os.chmod(path, 0o600)
        json.dump(manifest, stream, indent=2, ensure_ascii=True, allow_nan=False)
        stream.write('\n')
    verify(root)
    return manifest


def verify(root):
    root = Path(root)
    actual = read(root, 'manifest.json')
    expected = derive(root, actual)
    P.require(json.dumps(actual, sort_keys=True, allow_nan=False) == json.dumps(expected, sort_keys=True, allow_nan=False),
              'Manifest coverage/hash/relationship claims differ from verified payloads.')
    return actual


def finalize(root, final_directory, archive, source_root=None):
    root, final_directory, archive = Path(root), Path(final_directory), Path(archive)
    manifest = verify(root)
    if source_root is not None:
        S.ensure_head(source_root, manifest['repository']['commit'])
    digest = Path(str(archive) + '.manifest.sha256')
    P.require(root.resolve() != final_directory.resolve(), 'Staged and final directories must differ.')
    P.require(root.resolve() not in final_directory.resolve().parents
              and root.resolve() not in archive.resolve().parents, 'Final outputs cannot be inside the staged package.')
    P.require(all(not p.exists() and not p.is_symlink() for p in (final_directory, archive, digest)),
              'Refusing to overwrite a previous export.')
    P.require(final_directory.parent.name == 'exports' and final_directory.name not in {'', '.', '..'},
              'Unexpected final directory layout.')
    archive.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    final_directory.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    prefix = 'exports/' + final_directory.name + '/'
    descriptor, temporary_name = tempfile.mkstemp(prefix='.audit-', suffix='.partial.zip', dir=archive.parent)
    os.close(descriptor)
    temporary = Path(temporary_name)
    own_directory = own_archive = own_digest = False
    try:
        names = [entry['path'] for entry in manifest['payload_inventory']] + ['manifest.json']
        with zipfile.ZipFile(temporary, 'w', compression=zipfile.ZIP_DEFLATED) as bundle:
            for name in names:
                bundle.write(root / name, prefix + name)
        with zipfile.ZipFile(temporary) as bundle:
            P.require(len(bundle.namelist()) == len(names) and set(bundle.namelist()) == {prefix + n for n in names},
                      'ZIP payload inventory mismatch.')
            P.require(bundle.testzip() is None, 'ZIP integrity failure.')
            for name in names:
                P.require(bundle.read(prefix + name) == (root / name).read_bytes(), 'ZIP bytes differ from verified package.')
        verify(root)  # Catch source/payload changes while compression was in progress.
        if source_root is not None:
            S.ensure_head(source_root, manifest['repository']['commit'])
        # copytree creates only a new destination. Archive/digest use no-overwrite creation.
        final_directory.mkdir(mode=0o700)
        own_directory = True
        shutil.copytree(root, final_directory, dirs_exist_ok=True)
        verify(final_directory)
        os.link(temporary, archive)
        own_archive = True
        with digest.open('x', encoding='ascii') as stream:
            own_digest = True
            os.chmod(digest, 0o600)
            stream.write(hashlib.sha256((final_directory / 'manifest.json').read_bytes()).hexdigest() + '\n')
        shutil.rmtree(root)
    except BaseException:
        if own_digest:
            digest.unlink(missing_ok=True)
        if own_archive:
            archive.unlink(missing_ok=True)
        if own_directory:
            shutil.rmtree(final_directory)
        raise
    finally:
        temporary.unlink(missing_ok=True)
    return archive


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('seal', 'verify', 'finalize'))
    parser.add_argument('--package', required=True, type=Path)
    parser.add_argument('--final-directory', type=Path)
    parser.add_argument('--archive', type=Path)
    parser.add_argument('--source-root', type=Path)
    args = parser.parse_args()
    try:
        if args.action == 'seal':
            seal(args.package)
        elif args.action == 'verify':
            verify(args.package)
        else:
            P.require(args.final_directory is not None and args.archive is not None, 'Missing finalization targets.')
            finalize(args.package, args.final_directory, args.archive, args.source_root)
    except (P.ProjectError, R.P.ProjectError, PR.EvidenceError, R.PR.EvidenceError, S.SnapshotError,
            OSError, TypeError, ValueError, KeyError, AttributeError, zipfile.BadZipFile):
        print('ERROR: Package coverage/integrity/finalization failed; no successful export.', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
