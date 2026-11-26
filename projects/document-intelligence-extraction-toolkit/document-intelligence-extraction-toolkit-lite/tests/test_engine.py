import tempfile
import unittest
from pathlib import Path
from engine import extract_document

class ExtractionTests(unittest.TestCase):
    def test_markdown_metadata(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "note.md"
            path.write_text("# Summary\nMail a@b.com https://example.com", encoding="utf-8")
            result = extract_document(path)
            self.assertEqual(result["headings"], ["Summary"])
            self.assertEqual(result["emails"], ["a@b.com"])
            self.assertEqual(result["word_count"], 8)

    def test_unsupported_extension(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "image.png"
            path.write_bytes(b"x")
            with self.assertRaises(ValueError):
                extract_document(path)

if __name__ == "__main__":
    unittest.main()
