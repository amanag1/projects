"""Command-line interface for the Lite toolkit."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from .engine import build_manifest, find_duplicates, organize, write_manifest
except ImportError:
    from engine import build_manifest, find_duplicates, organize, write_manifest


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Preview and automate safe bulk file operations.")
    sub = parser.add_subparsers(dest="command", required=True)
    org = sub.add_parser("organize", help="Copy files into folders grouped by extension")
    org.add_argument("source", type=Path)
    org.add_argument("--output", type=Path, required=True)
    org.add_argument("--apply", action="store_true", help="Apply the copy plan (default: preview only)")
    manifest = sub.add_parser("manifest", help="Create a SHA-256 file manifest")
    manifest.add_argument("source", type=Path)
    manifest.add_argument("--output", type=Path, required=True)
    dup = sub.add_parser("duplicates", help="Find files with identical content")
    dup.add_argument("source", type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "organize":
            plan = organize(args.source, args.output, apply=args.apply)
            print(json.dumps({"mode": "apply" if args.apply else "dry-run", "files": plan}, indent=2))
        elif args.command == "manifest":
            write_manifest(args.source, args.output)
            print(f"Manifest written to {args.output}")
        else:
            print(json.dumps(find_duplicates(args.source), indent=2))
        return 0
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"Error: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
