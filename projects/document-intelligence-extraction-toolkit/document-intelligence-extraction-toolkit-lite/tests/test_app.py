import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class CliTests(unittest.TestCase):
    def test_cli_writes_json(self):
        root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "input.txt"
            output = Path(folder) / "out.json"
            source.write_text("hello world", encoding="utf-8")
            result = subprocess.run([sys.executable, str(root / "app.py"), str(source),
                                     "--output", str(output)], cwd=root, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(output.read_text())["total"], 1)


if __name__ == "__main__":
    unittest.main()
