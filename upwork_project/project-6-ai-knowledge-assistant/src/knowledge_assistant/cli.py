from __future__ import annotations
import argparse
from pathlib import Path
from .core import answer_from_evidence, read_text, split_passages

def main() -> None:
    parser = argparse.ArgumentParser(description="Ask a question against local TXT, MD or PDF files.")
    parser.add_argument("--folder", required=True, help="Folder containing source documents")
    parser.add_argument("--question", required=True)
    args = parser.parse_args()
    root = Path(args.folder)
    if not root.is_dir():
        parser.error(f"Not a directory: {root}")
    passages = []
    for path in sorted(root.iterdir()):
        if path.is_file() and path.suffix.lower() in {".txt", ".md", ".pdf"}:
            passages.extend(split_passages(read_text(path), path.name))
    result = answer_from_evidence(args.question, passages)
    print(result.answer)
    for source in result.sources:
        print(f"\n[SOURCE] {source.document} — passage {source.ordinal}")
    if result.needs_review:
        print("\n[REVIEW REQUIRED] No sufficiently reliable evidence was found.")

if __name__ == "__main__":
    main()
