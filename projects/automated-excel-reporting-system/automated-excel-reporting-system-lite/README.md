# Automated Excel Reporting System — Lite

CSV/XLSX in → profile, missing values, numeric summaries, and a formatted multi-sheet report.

## Install
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate | macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Usage
```bash
python app.py --help
```

Core module is `app.py`. Run tests with `pytest`. This edition intentionally keeps the dependency and deployment footprint small.
