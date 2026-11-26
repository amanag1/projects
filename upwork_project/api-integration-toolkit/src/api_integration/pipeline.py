"""Safe, vendor-neutral planning and validation for record integrations."""
from __future__ import annotations
from dataclasses import dataclass, asdict
import hashlib
import json
from typing import Any, Callable

@dataclass(frozen=True)
class RecordOutcome:
    record_id: str
    status: str
    message: str

def validate_record(record: dict[str, Any], required: tuple[str, ...]) -> list[str]:
    errors = []
    for field in required:
        if field not in record or record[field] is None or record[field] == "":
            errors.append(f"Missing required field: {field}")
    return errors

def map_record(record: dict[str, Any], mapping: dict[str, str]) -> dict[str, Any]:
    return {target: record.get(source) for source, target in mapping.items()}

def idempotency_key(record: dict[str, Any], key_fields: tuple[str, ...]) -> str:
    missing = [field for field in key_fields if field not in record]
    if missing:
        raise ValueError(f"Missing idempotency fields: {', '.join(missing)}")
    stable = {field: record[field] for field in sorted(key_fields)}
    payload = json.dumps(stable, sort_keys=True, default=str, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()

def plan_batch(records: list[dict[str, Any]], required: tuple[str, ...],
               mapping: dict[str, str], key_fields: tuple[str, ...]) -> list[dict[str, Any]]:
    planned = []
    seen: set[str] = set()
    for index, record in enumerate(records, start=1):
        errors = validate_record(record, required)
        if errors:
            planned.append({"index": index, "status": "rejected", "errors": errors, "payload": None})
            continue
        key = idempotency_key(record, key_fields)
        if key in seen:
            planned.append({"index": index, "status": "duplicate_in_batch", "idempotency_key": key, "payload": None})
            continue
        seen.add(key)
        planned.append({"index": index, "status": "ready", "idempotency_key": key,
                        "payload": map_record(record, mapping)})
    return planned

def execute_plan(plan: list[dict[str, Any]], writer: Callable[[dict[str, Any], str], Any],
                 dry_run: bool = True) -> list[RecordOutcome]:
    outcomes = []
    for item in plan:
        if item["status"] != "ready":
            outcomes.append(RecordOutcome(str(item["index"]), item["status"], "; ".join(item.get("errors", []))))
        elif dry_run:
            outcomes.append(RecordOutcome(str(item["index"]), "previewed", "No external write performed"))
        else:
            try:
                writer(item["payload"], item["idempotency_key"])
                outcomes.append(RecordOutcome(str(item["index"]), "written", "Target accepted record"))
            except Exception as exc:
                outcomes.append(RecordOutcome(str(item["index"]), "failed", type(exc).__name__))
    return outcomes
