from pathlib import Path
import pandas as pd
import pytest
from engine import profile_workbook

def test_profile_workbook_creates_report(tmp_path: Path):
    source, output = tmp_path / "input.xlsx", tmp_path / "report.xlsx"
    with pd.ExcelWriter(source) as writer:
        pd.DataFrame({"name": ["A", "B"], "score": [10, None]}).to_excel(writer, index=False, sheet_name="Data")
    result = profile_workbook(source, output)
    assert output.exists()
    assert result["sheets"][0]["rows"] == 2
    assert "Data_profile" in pd.ExcelFile(output).sheet_names

def test_missing_source_fails(tmp_path):
    with pytest.raises(FileNotFoundError):
        profile_workbook(tmp_path / "missing.xlsx", tmp_path / "out.xlsx")
