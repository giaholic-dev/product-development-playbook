"""Schema-2 full synthetic package and adversarial integrity/finalization cases."""

import copy
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

from test_audit_project import Fixture as ProjectFixture
from test_audit_records import Fixture as RecordsFixture
from test_audit_pr_evidence import Fixture as PRFixture, response

SPEC = importlib.util.spec_from_file_location('audit_package', Path(__file__).with_name('audit-package.py'))
K = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(K)
REPO = 'fixture/repo'


def write_provider_fixtures(destination, repository=REPO, populated=True):
    records = RecordsFixture(repository, populated=populated)
    K.R.write(K.R.collect(repository, transport=records), destination)
    project = ProjectFixture()
    project.items = project.items[:1]
    project.fields = [f for f in project.fields if f['dataType'] in K.P.SUPPORTED - {
        'LABELS', 'ASSIGNEES', 'LINKED_PULL_REQUESTS', 'REVIEWERS', 'REPOSITORY', 'MILESTONE'}]
    selected = {f['id'] for f in project.fields}
    project.values['I1'] = [v for v in project.values['I1'] if v['field']['id'] in selected]
    # If no local work records are selected, retain only external Project references.
    if not populated:
        project.items[0]['content']['repository']['nameWithOwner'] = 'external/repo'
    K.P.publish(K.P.collect('organization', 'fixture', 1, repository, project), destination)
    pr_fixture = PRFixture(numbers=())
    pr_fixture.routes = {'repos/' + repository: response({'id': 1, 'full_name': repository}),
                         'user': response({'id': 2, 'login': 'reader'})}
    K.PR.collect_evidence(repository, [], destination, pr_fixture)


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / 'repo'
        self.repo.mkdir()
        self.env = dict(os.environ, GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull,
                        GIT_AUTHOR_NAME='Fixture', GIT_AUTHOR_EMAIL='fixture@example.invalid',
                        GIT_COMMITTER_NAME='Fixture', GIT_COMMITTER_EMAIL='fixture@example.invalid')
        self.git('init', '-q')
        (self.repo / 'README.md').write_text('Committed source\n')
        (self.repo / '.gitignore').write_text('audit/\n')
        (self.repo / 'docs').mkdir()
        (self.repo / 'docs/guide.md').write_text('Guide\n')
        (self.repo / 'docs/link').symlink_to('../README.md')
        self.git('add', '-A')
        self.git('commit', '-qm', 'fixture')
        self.commit = self.git('rev-parse', 'HEAD').decode().strip()
        self.package = self.repo / 'audit/.staging/run'
        (self.package / 'github').mkdir(parents=True)
        (self.package / 'git').mkdir()
        K.S.export_snapshot(self.repo, self.commit, self.package / 'repository', reviewed=True)
        repository = self.package / 'repository'
        shutil.copyfile(repository / 'source/README.md', repository / 'README.md')
        shutil.copytree(repository / 'source/docs', repository / 'docs')
        (repository / 'config').mkdir()
        shutil.copyfile(repository / 'source/.gitignore', repository / 'config/.gitignore')
        source = K.read(self.package, 'repository/source-inventory.json')
        (repository / 'repository-tree.txt').write_text(''.join(json.dumps(e['path']) + '\n' for e in source['entries']))
        for name in ('branches.txt', 'tags.txt', 'recent-commits.tsv', 'status.txt'):
            (self.package / 'git' / name).write_text('fixture\n')
        write_provider_fixtures(self.package / 'github')
        command = '''source "$1"
OWNER=fixture
REPOSITORY=repo
REMOTE_IDENTITY=github.com/fixture/repo
BRANCH=fixture
DEFAULT_BRANCH=fixture
SELECTED_REF=fixture
DETACHED_HEAD=false
DIRTY=false
COMMIT="$3"
EXPORT_DIR="$2"
create_manifest
'''
        result = subprocess.run(['bash', '-euo', 'pipefail', '-c', command, 'fixture',
                                 str(Path(__file__).with_name('export-audit.sh')), str(self.package), self.commit],
                                capture_output=True, env=self.env)
        self.assertEqual(result.returncode, 0, result.stderr.decode())
        K.seal(self.package)

    def git(self, *args):
        return subprocess.run(['git', '-C', str(self.repo), *args], env=self.env,
                              check=True, capture_output=True).stdout

    def mutate(self, name, mutate):
        path = self.package / name
        data = json.loads(path.read_text())
        mutate(data)
        path.write_text(json.dumps(data))

    def assert_invalid(self):
        with self.assertRaises((K.P.ProjectError, K.R.P.ProjectError, K.PR.EvidenceError,
                                K.R.PR.EvidenceError, K.S.SnapshotError, OSError, KeyError, ValueError)):
            K.verify(self.package)

    def test_complete_derived_manifest_and_cli_offline_verify(self):
        manifest = K.verify(self.package)
        self.assertTrue(manifest['full_profile_complete'])
        self.assertEqual(manifest['contract'], 'audit-package-coverage/2.0.0')
        self.assertEqual(manifest['source_tree'], self.git('rev-parse', 'HEAD^{tree}').decode().strip())
        self.assertTrue(manifest['integrity']['source_tree_reconstructed'])
        self.assertTrue(any(c['name'] == 'discussions' and c['status'] == 'excluded' for c in manifest['collections']))
        self.assertNotIn('manifest.json', {p['path'] for p in manifest['payload_inventory']})
        result = subprocess.run([sys.executable, K.__file__, 'verify', '--package', str(self.package)], capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_payload_hash_corruption_is_rejected(self):
        path = self.package / 'git/status.txt'
        path.write_text('tampered\n')
        self.assert_invalid()

    def test_missing_required_and_extra_payload_are_rejected(self):
        original = (self.package / 'github/labels.json').read_bytes()
        (self.package / 'github/labels.json').unlink()
        self.assert_invalid()
        (self.package / 'github/labels.json').write_bytes(original)
        (self.package / 'github/unapproved.json').write_text('[]')
        self.assert_invalid()

    def test_manifest_major_counts_completeness_and_hash_controls(self):
        path = self.package / 'manifest.json'
        original = path.read_bytes()
        for mutation in (lambda m: m.update(schema_version='1.3.0'),
                         lambda m: m.update(schema_version='999.0.0'),
                         lambda m: m.update(full_profile_complete=False),
                         lambda m: m['repository'].update(dirty='false'),
                         lambda m: m['collection_pagination'].update(issues=1),
                         lambda m: m['collection_counts'].update(issues=999),
                         lambda m: m['payload_inventory'][0].update(sha256='0' * 64)):
            with self.subTest(mutation=mutation):
                path.write_bytes(original)
                self.mutate('manifest.json', mutation)
                self.assert_invalid()

    def test_source_tree_and_blob_identity_controls(self):
        path = self.package / 'repository/source-inventory.json'
        original = path.read_bytes()
        self.mutate('repository/source-inventory.json', lambda s: s['entries'][0].update(mode='100755'))
        self.assert_invalid()
        path.write_bytes(original)
        (self.package / 'repository/source/README.md').write_text('Different\n')
        self.assert_invalid()

    def test_symlinks_are_rejected_before_reads(self):
        path = self.package / 'github/issues.json'
        path.unlink()
        path.symlink_to(self.repo / 'README.md')
        self.assert_invalid()

    def test_partial_replay_and_foreign_local_references_fail(self):
        path = self.package / 'github/project-coverage.json'
        original = path.read_bytes()
        self.mutate('github/project-coverage.json', lambda c: c['observations'].pop())
        self.assert_invalid()
        path.write_bytes(original)
        self.mutate('github/issues.json', lambda issues: issues[0].update(node_id='foreign'))
        self.assert_invalid()

    def test_finalize_success_archive_and_manifest_digest(self):
        final = self.repo / 'audit/exports/run'
        archive = self.repo / 'audit/fixture.zip'
        K.finalize(self.package, final, archive)
        self.assertFalse(self.package.exists())
        K.verify(final)
        with zipfile.ZipFile(archive) as bundle:
            self.assertIsNone(bundle.testzip())
            self.assertEqual(bundle.read('exports/run/manifest.json'), (final / 'manifest.json').read_bytes())
        digest = Path(str(archive) + '.manifest.sha256').read_text().strip()
        self.assertEqual(digest, hashlib.sha256((final / 'manifest.json').read_bytes()).hexdigest())

    def test_zip_failure_and_copy_failure_leave_no_published_output(self):
        final, archive = self.repo / 'audit/exports/run', self.repo / 'audit/fixture.zip'
        with patch.object(K.zipfile, 'ZipFile', side_effect=OSError('fixture ZIP failure')):
            with self.assertRaises(OSError):
                K.finalize(self.package, final, archive)
        self.assertFalse(final.exists())
        self.assertFalse(archive.exists())
        self.assertEqual(list(archive.parent.glob('*.partial.zip')), [])
        with patch.object(K.shutil, 'copytree', side_effect=OSError('fixture copy failure')):
            with self.assertRaises(OSError):
                K.finalize(self.package, final, archive)
        self.assertFalse(final.exists())
        self.assertFalse(archive.exists())
        self.assertTrue(self.package.exists())

    def test_existing_run_is_preserved(self):
        final, archive = self.repo / 'audit/exports/run', self.repo / 'audit/fixture.zip'
        archive.write_bytes(b'previous')
        with self.assertRaises(K.P.ProjectError):
            K.finalize(self.package, final, archive)
        self.assertEqual(archive.read_bytes(), b'previous')
        self.assertTrue(self.package.exists())

    def test_prior_tool_and_project_evidence_versions_remain_readable(self):
        project_fixture = ProjectFixture()
        project_fixture.items = project_fixture.items[:1]
        project_fixture.fields = [f for f in project_fixture.fields if f['dataType'] in K.P.SUPPORTED - {
            'LABELS', 'ASSIGNEES', 'LINKED_PULL_REQUESTS', 'REVIEWERS', 'REPOSITORY', 'MILESTONE'}]
        selected = {f['id'] for f in project_fixture.fields}
        project_fixture.values['I1'] = [v for v in project_fixture.values['I1'] if v['field']['id'] in selected]
        old_project = K.P.collect('organization', 'fixture', 1, REPO, project_fixture, evidence_version='1.0.0')
        for name, value in old_project.items():
            (self.package / 'github' / name).write_text(json.dumps(value))
        self.mutate('manifest.json', lambda m: (m.update(tool_version='2.0.0'),
                    m['project_evidence'].update(evidence_schema_version='1.0.0')))
        K.seal(self.package)
        before = (self.package / 'github/project-requests.json').read_bytes()
        verified = K.verify(self.package)
        self.assertEqual(verified['tool_version'], '2.0.0')
        self.assertEqual((self.package / 'github/project-requests.json').read_bytes(), before)


if __name__ == '__main__':
    unittest.main()
