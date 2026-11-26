# Setup

## Local development
Use Python 3.11+, create a virtual environment, run `pip install -e ".[dev]"`, then `uvicorn fastapi_service.main:app --reload`.

## Docker Compose
Copy `.env.example` to `.env` and run `docker compose up --build`. The container uses a non-root account and a read-only root filesystem.

## Validation
Run `pytest -q` or `sh scripts/validate.sh`.
