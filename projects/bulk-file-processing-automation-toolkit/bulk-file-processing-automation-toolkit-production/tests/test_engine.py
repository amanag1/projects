from pathlib import Path
import pytest
from file_automation.engine.organizer import organize_directory, write_manifest


def test_organizes_and_manifests(tmp_path: Path):
    source = tmp_path / "in"
    source.mkdir()
    (source / "a.PDF").write_text("doc")
    (source / "README").write_text("plain")
    target = tmp_path / "out"
    copied = organize_directory(source, target)
    assert len(copied) == 2
    assert (target / "pdf" / "a.PDF").exists()
    manifest = target / "manifest.json"
    write_manifest(target, manifest)
    assert '"sha256"' in manifest.read_text()


def test_nested_destination_rejected(tmp_path: Path):
    source = tmp_path / "in"
    source.mkdir()
    with pytest.raises(ValueError):
        organize_directory(source, source / "nested")
