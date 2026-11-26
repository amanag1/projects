import tempfile
import unittest
from pathlib import Path
from app import main


class AppTests(unittest.TestCase):
    def test_manifest_command(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / "in"
            source.mkdir()
            (source / "a.txt").write_text("hello", encoding="utf-8")
            output = root / "manifest.json"
            self.assertEqual(main(["manifest", str(source), "--output", str(output)]), 0)
            self.assertTrue(output.exists())


if __name__ == "__main__":
    unittest.main()
