# FastAPI Starter Kit — Production

A modular FastAPI application foundation with settings, request correlation IDs, structured application logging, health/readiness endpoints, validation, tests, container configuration and a Helm starter chart.

## Local setup
Python 3.11+:
```bash
python -m venv .venv
pip install -e ".[dev]"
uvicorn fastapi_service.main:app --reload
```
Open `/docs` for the interactive API documentation.

## Container
```bash
cp .env.example .env
docker compose up --build
```

## Project design
- `api`: HTTP routes and schemas
- `core`: settings, logging and middleware
- `services`: application use cases
- `database`: persistence integration boundary
- `ui`: API documentation / optional frontend boundary

## Production hardening checklist
This is a strong starting structure, not a complete security certification. Before public deployment, configure authentication and authorization, secret storage, rate limits, CORS allow-lists, trusted proxy handling, database migrations, backups, tracing, metrics, alerting and resource policies. Replace example settings and review the container and Helm values for your environment.
