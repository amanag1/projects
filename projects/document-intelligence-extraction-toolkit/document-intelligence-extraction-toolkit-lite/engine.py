"""Dependency-free document extraction engine."""
from __future__ import annotations

import csv
import io
import re
from pathlib import Path

SUPPORTED = {".txt", ".md", ".csv"}
EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
URL_RE = re.compile(r"https?://[^\s<>\"']+", re.I)
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.M)


def _read_text(path: Path) -> str:
    raw = path.read_bytes()
    if path.suffix.lower() == ".csv":
        text = raw.decode("utf-8-sig")
        rows = csv.reader(io.StringIO(text))
        return "\n".join(" | ".join(row) for row in rows)
    return raw.decode("utf-8-sig")


def extract_document(path: str | Path) -> dict:
    file_path = Path(path)
    suffix = file_path.suffix.lower()
    if suffix not in SUPPORTED:
        raise ValueError(f"Unsupported file type: {suffix or '(no extension)'}")
    if not file_path.is_file():
        raise FileNotFoundError(str(file_path))
    text = _read_text(file_path)
    return {
        "filename": file_path.name,
        "extension": suffix,
        "size_bytes": file_path.stat().st_size,
        "character_count": len(text),
        "word_count": len(re.findall(r"\b\w+\b", text)),
        "headings": HEADING_RE.findall(text) if suffix == ".md" else [],
        "emails": sorted(set(EMAIL_RE.findall(text))),
        "urls": sorted(set(URL_RE.findall(text))),
        "text": text,
    }


def extract_many(paths: list[str | Path]) -> list[dict]:
    return [extract_document(path) for path in paths]
