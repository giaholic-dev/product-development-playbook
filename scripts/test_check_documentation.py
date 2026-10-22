"""Behavioral regression cases for documentation link failures and examples."""

import importlib.util
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("checker", Path(__file__).with_name("check-documentation.py"))
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class DocumentationChecks(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
