"""Command-line interface for Lite edition."""
import argparse
import json
from pathlib import Path

from engine import SUPPORTED, extract_document


def collect(path: Path, recursive: bool) -> list[Path]:
    if path.is_file():
        return [path]
    pattern = "**/*" if recursive else "*"
    return sorted(p for p in path.glob(pattern) if p.is_file() and p.suffix.lower() in SUPPORTED)


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract text and metadata from documents.")
    parser.add_argument("input", type=Path, help="A supported file or directory")
    parser.add_argument("--output", type=Path, help="Write JSON to this path")
    parser.add_argument("--recursive", action="store_true", help="Scan directories recursively")
    parser.add_argument("--pretty", action="store_true", help="Indent JSON output")
    args = parser.parse_args()
    if not args.input.exists():
        parser.error(f"Input does not exist: {args.input}")
    records = []
    errors = []
    for path in collect(args.input, args.recursive):
        try:
            records.append(extract_document(path))
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append({"filename": path.name, "error": str(exc)})
    payload = {"documents": records, "errors": errors, "total": len(records)}
    rendered = json.dumps(payload, indent=2 if args.pretty else None, ensure_ascii=False)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
