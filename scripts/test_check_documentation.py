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
