from automation_utilities.file_organizer import organize
from automation_utilities.folder_diff import compare_folders

def test_organizer_dry_run_does_not_move_files(tmp_path):
    source = tmp_path / "report.csv"
    source.write_text("id\n1\n")
    result = organize(tmp_path, dry_run=True)
    assert result[0]["status"] == "previewed"
    assert source.exists()

def test_folder_comparison_detects_changes(tmp_path):
    left, right = tmp_path / "left", tmp_path / "right"
    left.mkdir(); right.mkdir()
    (left / "same.txt").write_text("same")
    (right / "same.txt").write_text("same")
    (left / "changed.txt").write_text("old")
    (right / "changed.txt").write_text("new")
    (right / "extra.txt").write_text("extra")
    result = compare_folders(left, right)
    assert result["identical"] == ["same.txt"]
    assert result["changed"] == ["changed.txt"]
    assert result["only_right"] == ["extra.txt"]
