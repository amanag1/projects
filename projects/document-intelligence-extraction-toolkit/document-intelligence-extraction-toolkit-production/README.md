# Document Intelligence Toolkit — Production

A container-ready FastAPI service for extracting text and metadata from TXT, Markdown, CSV and text-based PDF files.

## Features
- `POST /api/v1/extract` accepts one multipart file and returns structured extraction results.
- `GET /health` and `GET /ready` provide liveness/readiness checks.
- Configurable upload-size limit, extension allow-list and request ID.
- PDF text extraction powered by pypdf.
- Docker Compose, CI workflow, Helm chart, tests and operations documentation.

## Run locally
Python 3.11+ is recommended.
```bash
python -m venv .venv
pip install -e ".[dev]"
uvicorn document_intelligence.main:app --reload
```
Open `/docs` for interactive API documentation.

## Extract
```bash
curl -X POST http://localhost:8000/api/v1/extract -F "file=@sample_data/example.md"
```
Docker: `docker compose up --build`.

## Limitations
PDF support extracts embedded text only. Scanned/image-only PDFs require OCR, which is not included. DOCX, spreadsheets and password-protected PDFs are not supported.

## Security
Uploads are read into memory, validated and never written to a user-controlled path or executed. Deploy behind authentication, rate limiting and network controls. Add quotas and asynchronous processing for high-volume use.
