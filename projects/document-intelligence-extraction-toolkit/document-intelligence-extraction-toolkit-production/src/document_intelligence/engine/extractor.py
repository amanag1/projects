from __future__ import annotations
import csv
import io
import re
from pathlib import Path
from pypdf import PdfReader

EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
URL_RE = re.compile(r"https?://[^\s<>\"']+", re.I)
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.M)
SUPPORTED = {".txt", ".md", ".csv", ".pdf"}

def extract_bytes(filename: str, content: bytes) -> dict:
    suffix = Path(filename).suffix.lower()
    if suffix not in SUPPORTED:
        raise ValueError("Unsupported file type")
    page_count = None
    if suffix == ".pdf":
        reader = PdfReader(io.BytesIO(content), strict=True)
        if reader.is_encrypted:
            raise ValueError("Password-protected PDFs are not supported")
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
        page_count = len(reader.pages)
    elif suffix == ".csv":
        decoded = content.decode("utf-8-sig")
        text = "\n".join(" | ".join(row) for row in csv.reader(io.StringIO(decoded)))
    else:
        text = content.decode("utf-8-sig")
    return {
        "filename": Path(filename).name, "extension": suffix, "size_bytes": len(content),
        "character_count": len(text), "word_count": len(re.findall(r"\b\w+\b", text)),
        "page_count": page_count, "headings": HEADING_RE.findall(text) if suffix == ".md" else [],
        "emails": sorted(set(EMAIL_RE.findall(text))), "urls": sorted(set(URL_RE.findall(text))),
        "text": text,
    }
