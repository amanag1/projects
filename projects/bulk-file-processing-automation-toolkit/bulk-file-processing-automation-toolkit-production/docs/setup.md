# Setup

## Local
Use Python 3.11+, create a virtual environment, run `pip install -e ".[dev]"`, then `uvicorn file_automation.main:app --reload`.

## Container
Copy `.env.example` to `.env` and run `docker compose up --build`. The container runs as a non-root user with a read-only root filesystem and a temporary writable filesystem.

## Tests
Run `pytest -q` or `sh scripts/validate.sh`.
