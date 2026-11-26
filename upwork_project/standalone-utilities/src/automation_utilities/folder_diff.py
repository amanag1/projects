"""Compare two folders by relative path and SHA-256; read-only."""
from __future__ import annotations
import hashlib
from pathlib import Path

def _digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def compare_folders(left: str | Path, right: str | Path) -> dict[str, list[str]]:
    a, b = Path(left), Path(right)
    if not a.is_dir() or not b.is_dir():
        raise NotADirectoryError("Both inputs must be existing directories")
    files_a = {p.relative_to(a).as_posix(): p for p in a.rglob("*") if p.is_file()}
    files_b = {p.relative_to(b).as_posix(): p for p in b.rglob("*") if p.is_file()}
    common = files_a.keys() & files_b.keys()
    return {
        "only_left": sorted(files_a.keys() - files_b.keys()),
        "only_right": sorted(files_b.keys() - files_a.keys()),
        "changed": sorted(name for name in common if _digest(files_a[name]) != _digest(files_b[name])),
        "identical": sorted(name for name in common if _digest(files_a[name]) == _digest(files_b[name])),
    }
