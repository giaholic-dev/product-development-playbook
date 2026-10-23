"""Behavioral tests use disposable repositories and synthetic data; no network."""

import importlib.util
import json
import os
import shutil
import zipfile
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("audit_source", Path(__file__).with_name("audit-source.py"))
SOURCE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SOURCE)


class SourceSnapshotTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        self.root.mkdir()
        self.env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull,
                        GIT_AUTHOR_NAME="Fixture", GIT_AUTHOR_EMAIL="fixture@example.invalid",
                        GIT_COMMITTER_NAME="Fixture", GIT_COMMITTER_EMAIL="fixture@example.invalid")
        self.run_git("init", "-q")
        self.run_git("config", "core.autocrlf", "false")
        self.run_git("config", "commit.gpgsign", "false")
        self.write("README.md", b"Committed readme\n")
        self.write(".gitignore", b"audit/\n")
        self.commit()
        self.output = Path(self.temp.name) / "snapshot"

    def run_git(self, *args, data=None):
        return subprocess.run(["git", "-C", str(self.root), *args], input=data,
                              env=self.env, check=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        return path

    def commit(self):
        self.run_git("add", "-A")
        self.run_git("commit", "-qm", "fixture")
        self.commit_id = self.run_git("rev-parse", "HEAD").decode().strip()

    def export(self, **options):
        return SOURCE.export_snapshot(self.root, self.commit_id, self.output, reviewed=True, **options)

    def test_committed_bytes_ignore_staged_unstaged_and_untracked(self):
        self.write("README.md", b"Staged edit")
        self.run_git("add", "README.md")
        self.write("README.md", b"Unstaged edit")
        self.write("untracked.txt", b"not authorized")
        inventory = self.export()
        self.assertTrue(inventory["dirty_initial"])
        self.assertFalse(inventory["working_tree_bytes_included"])
        self.assertEqual((self.output / "source/README.md").read_bytes(), b"Committed readme\n")
        self.assertFalse((self.output / "source/untracked.txt").exists())
        SOURCE.verify_snapshot(self.root, self.output)

    def test_complete_source_paths_binary_modes_and_newlines(self):
        for name in (".github/workflows/check.yml", ".devcontainer/config.json",
                     "scripts/tool.sh", "docs/space and\nnewline.bin"):
            self.write(name, b"\0\xff\n")
        os.chmod(self.root / "scripts/tool.sh", 0o755)
        self.commit()
        self.export()
        for name in (".github/workflows/check.yml", ".devcontainer/config.json",
                     "scripts/tool.sh", "docs/space and\nnewline.bin"):
            self.assertEqual((self.output / "source" / name).read_bytes(), b"\0\xff\n")
        inventory = SOURCE.verify_snapshot(self.root, self.output)
        mode = next(r["mode"] for r in inventory["entries"] if r["path"] == "scripts/tool.sh")
        self.assertEqual(mode, "100755")

    def test_symlink_blob_is_inert_and_does_not_read_external_target(self):
        external = Path(self.temp.name) / "private-target"
        external.write_bytes(b"must never be copied")
        (self.root / "docs").mkdir()
        (self.root / "docs/link").symlink_to(external)
        self.commit()
        self.export()
        target = self.output / "source/docs/link"
        self.assertFalse(target.is_symlink())
        self.assertEqual(target.read_bytes(), str(external).encode())
        SOURCE.verify_snapshot(self.root, self.output)

    def test_protected_files_and_tracked_output_are_inventoried_without_bytes(self):
        for name in (".env", ".ssh/id_ed25519", "keys/identity.PEM", "credentials.json"):
            self.write(name, b"private fixture")
        self.write("audit/old.zip", b"previous export")
        self.run_git("add", "-f", "audit/old.zip")
        self.commit()
        inventory = self.export()
        exclusions = {r["path"]: r for r in inventory["entries"] if r["disposition"] == "excluded"}
        self.assertEqual(len(exclusions), 5)
        self.assertFalse(inventory["all_tracked_blobs_retained"])
        for name, record in exclusions.items():
            self.assertFalse((self.output / "source" / name).exists())
            self.assertNotIn("sha256", record)
        SOURCE.verify_snapshot(self.root, self.output)

    def test_template_candidate_is_preserved_but_not_exempt_from_content_review(self):
        self.write(".env.example", b"API_KEY=replace-me\n")
        self.commit()
        self.export()
        self.assertEqual((self.output / "source/.env.example").read_bytes(), b"API_KEY=replace-me\n")

    def test_protected_required_source_fails_and_cleans_new_output(self):
        self.write(".github/private.key", b"private fixture")
        self.commit()
        with self.assertRaises(SOURCE.SnapshotError):
            self.export()
        self.assertFalse(self.output.exists())

    def test_suspected_secret_fails_without_logging_payload(self):
        token = b"ghp_" + b"A" * 40
        self.write("notes.txt", token)
        self.commit()
        with self.assertRaises(SOURCE.SnapshotError) as caught:
            self.export()
        self.assertNotIn(token.decode(), str(caught.exception))
        self.assertFalse(self.output.exists())

    def test_gitlink_is_explicit_and_not_fetched(self):
        self.run_git("update-index", "--add", "--cacheinfo", "160000", self.commit_id, "vendor/component")
        self.run_git("commit", "-qm", "gitlink")
        self.commit_id = self.run_git("rev-parse", "HEAD").decode().strip()
        inventory = self.export()
        record = next(r for r in inventory["entries"] if r["path"] == "vendor/component")
        self.assertEqual(record["disposition"], "gitlink-only")
        self.assertFalse((self.output / "source/vendor/component").exists())

    def test_lfs_pointer_is_explicit_and_required_missing_content_fails(self):
        pointer = b"version https://git-lfs.github.com/spec/v1\noid sha256:" + b"0" * 64 + b"\nsize 12\n"
        self.write("assets/data.bin", pointer)
        self.commit()
        inventory = self.export()
        self.assertEqual(next(r["disposition"] for r in inventory["entries"]
                              if r["path"] == "assets/data.bin"), "lfs-pointer-only")
        self.output = Path(self.temp.name) / "required-snapshot"
        self.write("docs/data.bin", pointer)
        self.commit()
        with self.assertRaises(SOURCE.SnapshotError):
            self.export()
        self.assertFalse(self.output.exists())

    def test_tampered_or_missing_payload_fails_verification(self):
        self.export()
        path = self.output / "source/README.md"
        path.write_bytes(b"tampered")
        with self.assertRaises(SOURCE.SnapshotError):
            SOURCE.verify_snapshot(self.root, self.output)
        path.unlink()
        with self.assertRaises(SOURCE.SnapshotError):
            SOURCE.verify_snapshot(self.root, self.output)

    def test_tampered_inventory_and_extra_payload_fail(self):
        self.export()
        path = self.output / "source-inventory.json"
        original = path.read_text()
        inventory = json.loads(original)
        inventory["entries"] = []
        path.write_text(json.dumps(inventory))
        with self.assertRaises(SOURCE.SnapshotError):
            SOURCE.verify_snapshot(self.root, self.output)
        path.write_text(original)
        (self.output / "source/extra").write_bytes(b"extra")
        with self.assertRaises(SOURCE.SnapshotError):
            SOURCE.verify_snapshot(self.root, self.output)

    def test_substituted_symlink_fails_without_reading_target(self):
        self.export()
        target = self.output / "source/README.md"
        target.unlink()
        target.symlink_to(self.root / "README.md")
        with self.assertRaises(SOURCE.SnapshotError):
            SOURCE.verify_snapshot(self.root, self.output)

    def test_head_change_during_export_fails_and_cleans_output(self):
        original = SOURCE.describe
        changed = False

        def change_head(root, entry, output):
            nonlocal changed
            result = original(root, entry, output)
            if not changed:
                changed = True
                self.write("new.txt", b"new revision")
                self.commit()
            return result

        selected = self.commit_id
        with patch.object(SOURCE, "describe", side_effect=change_head):
            with self.assertRaises(SOURCE.SnapshotError):
                SOURCE.export_snapshot(self.root, selected, self.output, reviewed=True)
        self.assertFalse(self.output.exists())

    def test_overwrite_and_unreviewed_source_are_rejected(self):
        with self.assertRaises(SOURCE.SnapshotError):
            SOURCE.export_snapshot(self.root, self.commit_id, self.output)
        self.export()
        sentinel = (self.output / "source/README.md").read_bytes()
        with self.assertRaises(SOURCE.SnapshotError):
            self.export()
        self.assertEqual((self.output / "source/README.md").read_bytes(), sentinel)

    def test_missing_blob_and_invalid_paths_fail_safely(self):
        with patch.object(SOURCE, "git", side_effect=SOURCE.SnapshotError("Missing blob")):
            with self.assertRaises(SOURCE.SnapshotError):
                self.export()
        for name in ("../escape", "/absolute", "a/../b", "a\\b", "a//b"):
            with self.assertRaises(SOURCE.SnapshotError):
                SOURCE.safe_path(name)
        with self.assertRaises(SOURCE.SnapshotError):
            SOURCE.export_snapshot(self.root, "--help", self.output, reviewed=True)

    def test_case_colliding_paths_are_rejected_before_write(self):
        oid = self.run_git("hash-object", "-w", "--stdin", data=b"fixture").decode().strip()
        self.run_git("update-index", "--add", "--cacheinfo", "100644", oid, "Case.txt")
        self.run_git("update-index", "--add", "--cacheinfo", "100644", oid, "case.txt")
        self.run_git("commit", "-qm", "colliding paths")
        self.commit_id = self.run_git("rev-parse", "HEAD").decode().strip()
        with self.assertRaises(SOURCE.SnapshotError):
            self.export()
        self.assertFalse(self.output.exists())


    @unittest.skipUnless(all(shutil.which(c) for c in ("jq",)),
                         "Synthetic packaging needs jq")
    def test_bash_integration_packages_committed_bytes_and_source_manifest(self):
        self.write("docs/guide.md", b"Committed guide")
        self.write(".github/workflows/fixture.yml", b"name: fixture")
        self.write("scripts/fixture.sh", b"#!/bin/sh\nexit 0\n")
        self.commit()
        self.write("README.md", b"Local edit excluded")
        exporter = Path(__file__).with_name("export-audit.sh").resolve()
        from test_audit_package import write_provider_fixtures
        project_fixture = self.root / "project-fixture"
        write_provider_fixtures(project_fixture, "fixture/fixture", populated=False)
        command = r'''
source "$1"
ROOT="$2"
COMMIT="$3"
BRANCH=fixture
DEFAULT_BRANCH=fixture
SELECTED_REF=fixture
DETACHED_HEAD=false
DIRTY=true
OWNER=fixture
REPOSITORY=fixture
PROJECT_OWNER=fixture
PROJECT_OWNER_KIND=organization
PROJECT_NUMBER=1
REMOTE_IDENTITY=github.com/fixture/fixture
TIMESTAMP=fixture
EXPORT_ROOT=audit
FINAL_EXPORT_DIR=audit/exports/fixture
STAGING_DIR=audit/.staging/fixture
EXPORT_DIR="$STAGING_DIR"
ZIP_FILE=audit/fixture.zip
create_directories
export_repository
export_branches
export_tags
export_recent_commits
export_repository_status
cp "$ROOT"/project-fixture/*.json "$EXPORT_DIR/github/"
create_manifest
seal_manifest
validate_integrity
compress
'''
        subprocess.run(["bash", "-euo", "pipefail", "-c", command, "fixture",
                        str(exporter), str(self.root), self.commit_id],
                       cwd=self.root, env=self.env, check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        with zipfile.ZipFile(self.root / "audit/fixture.zip") as archive:
            prefix = "exports/fixture/"
            self.assertEqual(archive.read(prefix + "repository/README.md"), b"Committed readme\n")
            self.assertEqual(archive.read(prefix + "repository/source/scripts/fixture.sh"),
                             b"#!/bin/sh\nexit 0\n")
            self.assertEqual(archive.read(prefix + "repository/docs/guide.md"), b"Committed guide")
            manifest = json.loads(archive.read(prefix + "manifest.json"))
            self.assertEqual(manifest["schema_version"], "2.0.0")
            self.assertEqual(manifest["source_snapshot"]["commit"], self.commit_id)
            self.assertTrue(manifest["full_profile_complete"])
            self.assertFalse(manifest["source_snapshot"]["working_tree_bytes_included"])


if __name__ == "__main__":
    unittest.main()
