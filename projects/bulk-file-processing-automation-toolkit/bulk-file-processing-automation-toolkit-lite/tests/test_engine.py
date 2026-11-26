import tempfile
import unittest
from pathlib import Path

from engine import build_manifest, find_duplicates, organize, plan_organization


class EngineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.source.mkdir()
        (self.source / "one.txt").write_text("same", encoding="utf-8")
        (self.source / "two.txt").write_text("same", encoding="utf-8")
        (self.source / "photo.JPG").write_bytes(b"image")

    def tearDown(self):
        self.temp.cleanup()

    def test_plan_groups_by_lowercase_extension(self):
        plan = plan_organization(self.source, self.root / "out")
        self.assertEqual([Path(x["destination"]).parent.name for x in plan], ["jpg", "txt", "txt"])

    def test_default_is_preview_and_apply_copies(self):
        output = self.root / "out"
        plan = organize(self.source, output)
        self.assertEqual(len(plan), 3)
        self.assertFalse(output.exists())
        organize(self.source, output, apply=True)
        self.assertEqual(len(list(output.rglob("*.*"))), 3)

    def test_manifest_and_duplicate_detection(self):
        self.assertEqual(len(build_manifest(self.source)), 3)
        self.assertEqual(len(find_duplicates(self.source)), 1)

    def test_nested_or_same_output_rejected(self):
        with self.assertRaises(ValueError):
            plan_organization(self.source, self.source / "out")


if __name__ == "__main__":
    unittest.main()
