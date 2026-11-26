"""Preview-first file organizer. Does not overwrite existing files."""
from __future__ import annotations
from pathlib import Path
import shutil

def plan_organization(folder: str | Path) -> list[tuple[Path, Path]]:
    root = Path(folder)
    if not root.is_dir():
        raise NotADirectoryError(root)
    plan = []
    for source in sorted(p for p in root.iterdir() if p.is_file()):
        target_dir = root / (source.suffix.lower().lstrip(".") or "no_extension")
        target = target_dir / source.name
        if target.exists():
            target = target_dir / f"{source.stem}_{source.stat().st_size}{source.suffix}"
        plan.append((source, target))
    return plan

def organize(folder: str | Path, dry_run: bool = True) -> list[dict[str, str]]:
    results = []
    for source, target in plan_organization(folder):
        status = "previewed"
        if not dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                status = "skipped_collision"
            else:
                shutil.move(str(source), str(target))
                status = "moved"
        results.append({"source": str(source), "target": str(target), "status": status})
    return results
