# Setup

Requires Python 3.10+.

```bash
python -m venv .venv
# Activate the environment, then:
pip install -e ".[test]"
uvicorn excel_reporting.main:app --app-dir src --reload
pytest -q
```

Container: `docker compose up --build`. API health check: `GET /health`. Upload a workbook to `POST /api/v1/reports/profile` using multipart field `file`.
