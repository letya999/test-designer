"""Regression checks for public authoring validation and payload isolation."""

import tempfile
import unittest
import zipfile
from pathlib import Path

from validate import ROOT, frontmatter, package, validate


class ValidationTests(unittest.TestCase):
    def test_real_repository(self):
        payload = validate(ROOT)
        self.assertIn(ROOT / "LICENSE", payload)
        self.assertNotIn(ROOT / "README.ru.md", payload)
        self.assertTrue(all(p == ROOT / "SKILL.md" or p == ROOT / "LICENSE"
                            or p.parent == ROOT / "references" for p in payload))

    def test_frontmatter_rejects_missing_header_and_non_mapping(self):
        for text in ("name: example", "---\n- list\n---\n"):
            with self.subTest(text=text), self.assertRaises((TypeError, ValueError)):
                frontmatter(text)

    def test_frontmatter_preserves_folded_description(self):
        self.assertEqual(frontmatter("---\nname: sample\ndescription: >-\n  two\n  words\n---\n")
                         ["description"], "two words")

    def test_archive_has_exact_bytes_and_excludes_repository_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name, content in {"SKILL.md": b"subject\n", "LICENSE": b"MIT\n",
                                  "README.md": b"not a runtime file"}.items():
                (root / name).write_bytes(content)
            archive = package(root, [root / "SKILL.md", root / "LICENSE"])
            with zipfile.ZipFile(archive) as output:
                self.assertEqual(set(output.namelist()),
                                 {"test-designer/SKILL.md", "test-designer/LICENSE"})
                self.assertEqual(output.read("test-designer/SKILL.md"), b"subject\n")
                self.assertIsNone(output.testzip())

    def test_stale_staging_file_fails_without_deleting_it(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "SKILL.md").write_text("source", encoding="utf-8")
            extra = root / "dist/test-designer/private.txt"
            extra.parent.mkdir(parents=True)
            extra.write_text("must not ship", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Stale"):
                package(root, [root / "SKILL.md"])
            self.assertTrue(extra.exists())


if __name__ == "__main__":
    unittest.main()
