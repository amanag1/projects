"""Command-line entry points for the standalone utilities."""
from __future__ import annotations
import argparse
import json
from .csv_audit import audit_csv
from .file_organizer import organize
from .folder_diff import compare_folders

def main() -> None:
    parser = argparse.ArgumentParser(prog="automation-utils")
    sub = parser.add_subparsers(dest="command", required=True)
    csv_cmd = sub.add_parser("csv-audit")
    csv_cmd.add_argument("file")
    csv_cmd.add_argument("--required", default="")
    csv_cmd.add_argument("--duplicate-key", default="")
    org_cmd = sub.add_parser("organize")
    org_cmd.add_argument("folder")
    org_cmd.add_argument("--apply", action="store_true", help="Move files; default is preview only")
    diff_cmd = sub.add_parser("folder-diff")
    diff_cmd.add_argument("left")
    diff_cmd.add_argument("right")
    args = parser.parse_args()
    if args.command == "csv-audit":
        result = audit_csv(args.file, tuple(filter(None, args.required.split(","))),
                           tuple(filter(None, args.duplicate_key.split(","))))
    elif args.command == "organize":
        result = organize(args.folder, dry_run=not args.apply)
    else:
        result = compare_folders(args.left, args.right)
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
