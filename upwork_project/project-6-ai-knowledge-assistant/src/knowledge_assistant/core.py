"""Small, dependency-light retrieval layer with traceable source passages."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import re

@dataclass(frozen=True)
class Passage:
    document: str
    text: str
    ordinal: int

@dataclass(frozen=True)
class EvidenceAnswer:
    question: str
    answer: str
    sources: tuple[Passage, ...]
    needs_review: bool

def read_text(path: str | Path) -> str:
    p = Path(path)
    suffix = p.suffix.lower()
    if suffix in {".txt", ".md"}:
        return p.read_text(encoding="utf-8")
    if suffix == ".pdf":
        try:
            from pypdf import PdfReader
        except ImportError as exc:
            raise RuntimeError("Install the optional PDF dependency: pip install -e '.[pdf]'") from exc
        reader = PdfReader(str(p))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    raise ValueError(f"Unsupported document type: {suffix}")

def split_passages(text: str, document: str, words_per_chunk: int = 120) -> list[Passage]:
    if words_per_chunk < 20:
        raise ValueError("words_per_chunk must be at least 20")
    words = text.split()
    return [Passage(document, " ".join(words[i:i + words_per_chunk]), n)
            for n, i in enumerate(range(0, len(words), words_per_chunk), start=1)]

def _terms(value: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]{2,}", value.lower()))

def retrieve(question: str, passages: list[Passage], limit: int = 3) -> list[Passage]:
    if not question.strip():
        raise ValueError("question must not be empty")
    if limit < 1:
        raise ValueError("limit must be positive")
    query = _terms(question)
    ranked = []
    for p in passages:
        overlap = len(query & _terms(p.text))
        if overlap:
            ranked.append((overlap, p))
    ranked.sort(key=lambda item: (-item[0], item[1].document, item[1].ordinal))
    return [p for _, p in ranked[:limit]]

def answer_from_evidence(question: str, passages: list[Passage], min_overlap: int = 1) -> EvidenceAnswer:
    matches = retrieve(question, passages)
    if not matches:
        return EvidenceAnswer(question, "I could not find supporting information in the supplied documents.", (), True)
    q = _terms(question)
    score = max(len(q & _terms(p.text)) for p in matches)
    if score < min_overlap:
        return EvidenceAnswer(question, "Insufficient evidence. Please review the source documents.", tuple(matches), True)
    # Extractive mode deliberately returns source text rather than fabricating a synthesis.
    return EvidenceAnswer(question, " ".join(p.text for p in matches), tuple(matches), False)
