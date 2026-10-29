"""Behavioral regression cases for documentation link failures and examples."""

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("checker", Path(__file__).with_name("check-documentation.py"))
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class DocumentationChecks(unittest.TestCase):
    def test_archived_and_staged_exports_do_not_change_maintained_result(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'README.md').write_text('[guide](docs/guide.md)\n')
            (root / 'docs').mkdir()
            (root / 'docs/guide.md').write_text('# Guide\n')
            before = checker.check(root)
            archived = {}
            for output in ('audit/exports/run', 'audit/.staging/run-pid'):
                for relative in ('repository/README.md', 'repository/docs/guide.md',
                                 'repository/source/README.md', 'repository/source/docs/guide.md'):
                    path = root / output / relative
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text('[archive-only](absent.md)\n')
                    archived[path] = path.read_bytes()
            self.assertEqual(checker.check(root), before)
            self.assertEqual({p: p.read_bytes() for p in archived}, archived)
            (root / 'docs/guide.md').write_text('[maintained](missing.md)\n')
            self.assertIn('docs/guide.md:1: missing target: missing.md', checker.check(root)[2])

    def test_output_exclusions_are_anchored_and_do_not_hide_audit_docs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for relative in ('audit/README.md', 'docs/audit/exports/notes.md', 'exports/notes.md'):
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('[broken](missing.md)\n')
            files, _, errors = checker.check(root)
            self.assertEqual(len(files), 3)
            self.assertEqual(len(errors), 3)

    def test_non_git_cli_root_preserves_explicit_archive_inspection(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'README.md').write_text('# Maintained\n')
            archive = root / 'audit/exports/run/repository'
            archive.mkdir(parents=True)
            (archive / 'README.md').write_text('[broken](missing.md)\n')
            script = Path(checker.__file__)
            result = subprocess.run([sys.executable, str(script), '--root', str(root)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('Checked 1 Markdown files', result.stdout)
            # --root defines a new boundary, so an explicitly selected archived
            # source can still be checked without changing its bytes.
            result = subprocess.run([sys.executable, str(script), '--root', str(archive)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn('README.md:1: missing target: missing.md', result.stderr)

    def run_case(self, source, target="# Valid\n"):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text(source)
            (root / "target.md").write_text(target)
            return checker.check(root)[2]

    def test_missing_file_fails(self):
        self.assertTrue(self.run_case("[broken](missing.md)"))

    def test_missing_fragment_fails(self):
        self.assertTrue(self.run_case("[broken](target.md#missing)"))

    def test_valid_fragment_and_duplicate_heading(self):
        self.assertFalse(self.run_case("[one](target.md#valid) [two](target.md#valid-1)", "# Valid\n# Valid\n"))

    def test_examples_are_not_links(self):
        self.assertFalse(self.run_case("```md\n[example](absent.md)\n```\n~~~md\n[example](absent.md)\n~~~\n`[example](absent.md)`\n    [example](absent.md)\n"))

    def test_external_urls_are_not_fetched(self):
        self.assertFalse(self.run_case("[external](https://example.invalid/a#b)"))

    def test_reference_links_are_checked(self):
        self.assertFalse(self.run_case("[link][owner]\n\n[owner]: target.md#valid\n"))
        self.assertTrue(self.run_case("[link][absent]"))
        self.assertTrue(self.run_case("[link][owner]\n\n[owner]: missing.md\n"))

    def test_repository_escape_fails(self):
        self.assertTrue(self.run_case("[escape](../outside.md)"))

    def test_reference_labels_normalize_case_and_whitespace(self):
        for source in (
            "[go][OWNER]\n\n[owner]: target.md#valid\n",
            "[go][  Product\t OWNER ]\n\n[product owner]: target.md\n",
            "[go][product owner]\n\n[ Product   OWNER ]: target.md\n",
            "[Product  OWNER][]\n\n[product owner]: target.md\n",
            "![image][OWNER]\n\n[owner]: target.md\n",
            "[go][STRASSE]\n\n[Straße]: target.md\n",
        ):
            with self.subTest(source=source):
                self.assertFalse(self.run_case(source))
        self.assertTrue(self.run_case("[go][ OTHER  owner ]\n\n[owner]: target.md\n"))

    def test_first_normalized_reference_definition_wins(self):
        for first, second, fails in (
            ('missing.md', 'target.md', True),
            ('target.md', 'missing.md', False),
            ('target.md#missing', 'target.md#valid', True),
            ('target.md#valid', 'target.md#missing', False),
        ):
            for labels in (('owner', 'owner'), (' OWNER ', 'owner'), ('Product  OWNER', 'product\towner')):
                with self.subTest(first=first, second=second, labels=labels):
                    source = f"[go][{labels[1]}]\n\n[{labels[0]}]: {first}\n[{labels[1]}]: {second}\n"
                    self.assertEqual(bool(self.run_case(source)), fails)

    def test_code_example_definition_cannot_override_real_reference(self):
        source = "[go][OWNER]\n\n[owner]: missing.md\n```md\n[OWNER]: target.md\n```\n"
        self.assertTrue(self.run_case(source))
        self.assertFalse(self.run_case(source.replace('missing.md', 'target.md')))


if __name__ == "__main__":
    unittest.main()
