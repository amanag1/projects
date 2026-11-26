from pathlib import Path
import pandas as pd

def build_profile(source: Path, destination: Path) -> dict:
    if not source.is_file():
        raise FileNotFoundError(source)
    sheets = pd.read_excel(source, sheet_name=None)
    if not sheets:
        raise ValueError("Workbook contains no worksheets")
    details = []
    with pd.ExcelWriter(destination, engine="openpyxl") as writer:
        for sheet, frame in sheets.items():
            base = str(sheet)[:22]
            frame.to_excel(writer, sheet_name=str(sheet)[:31], index=False)
            profile = pd.DataFrame({
                "column": frame.columns.astype(str),
                "dtype": [str(x) for x in frame.dtypes],
                "missing": [int(x) for x in frame.isna().sum()],
                "distinct": [int(x) for x in frame.nunique(dropna=True)],
            })
            profile.to_excel(writer, sheet_name=f"{base}_profile"[:31], index=False)
            details.append({"sheet": str(sheet), "rows": len(frame), "columns": len(frame.columns)})
    return {"sheets": details, "output_file": destination.name}
