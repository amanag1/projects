# Automated Excel Reporting System — Production

A modular FastAPI service that accepts Excel workbooks and returns a profiled workbook with original worksheet data and column-level diagnostics (data type, missing count and distinct count).

## Run locally
```bash
pip install -e ".[test]"
uvicorn excel_reporting.main:app --app-dir src --reload
pytest -q
```

## Run with a container
```bash
docker compose up --build
```

- Health: `GET /health`
- Readiness: `GET /ready`
- Generate report: `POST /api/v1/reports/profile` (multipart field: `file`)

Helm chart: `deploy/helm/excel-reporting`. Before internet-facing deployment, add authentication, upload-size enforcement, malware scanning, managed artifact storage and retention policies.
