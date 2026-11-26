# Automated Excel Reporting System — Lite

A lightweight, local tool that reads an Excel workbook and creates a second workbook containing the original sheets plus per-column data profiles (type, missing values and distinct values).

## Run
```bash
python -m pip install -r requirements.txt
python app.py sample_data/sales.xlsx --output output/report.xlsx
```

## Test
```bash
python -m pip install pytest
pytest -q
```

Python 3.10+. Input files are read only; the output is written separately. This edition runs locally and does not include an API, database, container or cluster deployment.
