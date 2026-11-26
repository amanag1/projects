# Bulk File Processing Toolkit — Production

A container-ready FastAPI service that accepts a bounded batch of uploaded files, organizes them by extension, and returns a ZIP archive. Each request receives an isolated temporary workspace.

## Run locally
```bash
python -m venv .venv
# Activate the environment, then:
pip install -e ".[dev]"
uvicorn file_automation.main:app --reload
```
Open `/docs` for the API schema. Health endpoint: `/health`.

## Process a batch
Send multipart files to `POST /api/v1/process`. The response is a ZIP containing extension folders and a SHA-256 manifest.

## Container
```bash
docker compose up --build
```

## Configuration
- `MAX_UPLOAD_MB`: maximum combined uploaded bytes (default 25)
- `MAX_FILES_PER_BATCH`: maximum files in one request (default 50)

## Operational boundaries
This is a synchronous API starter, not a durable background queue. Temporary workspaces are removed after the response is sent. Add authentication, rate limiting, request quotas, malware scanning, persistent object storage, observability and an explicit retention policy before internet-facing deployment. Do not mount sensitive host directories into the service.
