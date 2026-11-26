"""Reusable Excel profiling and report generation functions."""
from pathlib import Path
import pandas as pd

def profile_workbook(source: str | Path, output: str | Path) -> dict:
    source, output = Path(source), Path(output)
    if not source.is_file():
        raise FileNotFoundError(source)
    sheets = pd.read_excel(source, sheet_name=None)
    if not sheets:
        raise ValueError("Workbook contains no worksheets")
    summary = []
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        for name, frame in sheets.items():
            safe_name = str(name)[:31]
            frame.to_excel(writer, sheet_name=safe_name, index=False)
            stats = pd.DataFrame({
                "column": frame.columns.astype(str),
                "dtype": [str(t) for t in frame.dtypes],
                "missing": [int(v) for v in frame.isna().sum()],
                "unique": [int(v) for v in frame.nunique(dropna=True)],
            })
            stats.to_excel(writer, sheet_name=(safe_name[:22] + "_profile")[:31], index=False)
            summary.append({"sheet": name, "rows": len(frame), "columns": len(frame.columns)})
    return {"output": str(output), "sheets": summary}
