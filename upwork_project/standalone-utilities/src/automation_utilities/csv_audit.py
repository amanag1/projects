"""Audit CSV structure and data quality; never modify the source file."""
from __future__ import annotations
import csv
from collections import Counter
from pathlib import Path
from typing import Any

def audit_csv(path: str | Path, required_columns: tuple[str, ...] = (),
              duplicate_key: tuple[str, ...] = ()) -> dict[str, Any]:
    source = Path(path)
    with source.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames or []
        missing = [name for name in required_columns if name not in headers]
        rows = list(reader)
    duplicates = []
    if duplicate_key and not missing:
        keys = [tuple((row.get(k) or "").strip().casefold() for k in duplicate_key) for row in rows]
        counts = Counter(keys)
        duplicates = [{"key": list(key), "count": count} for key, count in counts.items() if count > 1]
    null_counts = {name: sum(1 for row in rows if not (row.get(name) or "").strip()) for name in headers}
    return {"file": source.name, "row_count": len(rows), "columns": headers,
            "missing_required_columns": missing, "blank_counts": null_counts,
            "duplicate_groups": duplicates, "passed": not missing}
