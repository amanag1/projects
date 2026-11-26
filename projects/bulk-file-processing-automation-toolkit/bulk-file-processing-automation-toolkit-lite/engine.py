"""Safe file discovery, organization and content manifest operations."""
from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path
from typing import Iterable


def discover_files(source: Path, ignored_names: Iterable[str] = ()) -> list[Path]:
    source = source.expanduser().resolve()
    if not source.is_dir():
        raise ValueError(f"Source directory does not exist: {source}")
    ignored = set(ignored_names)
    return sorted(
        (p for p in source.rglob("*") if p.is_file() and p.name not in ignored),
        key=lambda p: str(p).lower(),
    )


def category_for(path: Path) -> str:
    suffix = path.suffix.lower().lstrip(".")
    return suffix if suffix else "no_extension"


def unique_destination(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10000):
        candidate = path.with_name(f"{path.stem}_{index}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise RuntimeError(f"Could not find a free destination for {path.name}")


def plan_organization(source: Path, output: Path) -> list[dict[str, str]]:
    source = source.expanduser().resolve()
    output = output.expanduser().resolve()
    if source == output or source in output.parents or output in source.parents:
        raise ValueError("Source and output directories must be separate, non-nested paths")
    plan = []
    for item in discover_files(source):
        destination = unique_destination(output / category_for(item) / item.name)
        plan.append({"source": str(item), "destination": str(destination)})
    return plan


def organize(source: Path, output: Path, apply: bool = False) -> list[dict[str, str]]:
    plan = plan_organization(source, output)
    if apply:
        for item in plan:
            destination = Path(item["destination"])
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item["source"], destination)
    return plan


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_manifest(source: Path) -> list[dict[str, object]]:
    records = []
    for path in discover_files(source):
        records.append({
            "path": str(path.relative_to(source.resolve())),
            "size_bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        })
    return records


def find_duplicates(source: Path) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}
    for record in build_manifest(source):
        groups.setdefault(str(record["sha256"]), []).append(str(record["path"]))
    return {digest: paths for digest, paths in groups.items() if len(paths) > 1}


def write_manifest(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(build_manifest(source), indent=2), encoding="utf-8")
