"""Filesystem operations isolated from the HTTP layer."""
from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path


def file_category(path: Path) -> str:
    return path.suffix.lower().lstrip(".") or "no_extension"


def organize_directory(source: Path, destination: Path) -> list[Path]:
    source = source.resolve()
    destination = destination.resolve()
    if source == destination or source in destination.parents or destination in source.parents:
        raise ValueError("Source and destination must be separate, non-nested directories")
    destination.mkdir(parents=True, exist_ok=True)
    copied = []
    for item in sorted(source.rglob("*")):
        if not item.is_file():
            continue
        folder = destination / file_category(item)
        folder.mkdir(parents=True, exist_ok=True)
        target = folder / item.name
        if target.exists():
            target = folder / f"{item.stem}_{len(copied) + 1}{item.suffix}"
        shutil.copy2(item, target)
        copied.append(target)
    return copied


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_manifest(root: Path, destination: Path) -> None:
    records = []
    for item in sorted(root.rglob("*")):
        if item.is_file() and item.resolve() != destination.resolve():
            records.append({
                "path": str(item.relative_to(root)),
                "size_bytes": item.stat().st_size,
                "sha256": sha256_file(item),
            })
    destination.write_text(json.dumps(records, indent=2), encoding="utf-8")
