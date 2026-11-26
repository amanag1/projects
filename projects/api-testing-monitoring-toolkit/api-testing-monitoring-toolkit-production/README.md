# API Testing & Monitoring Toolkit — Production

A modular FastAPI service for running HTTP endpoint checks. Supports method, expected status, custom headers, bounded timeout and optional JSON field assertions. Results include duration and pass/fail.

```bash
pip install -e ".[test]"
uvicorn api_monitoring.main:app --app-dir src --reload
pytest -q
```

Container: `docker compose up --build`

- Health: `GET /health`
- Readiness: `GET /ready`
- Execute check: `POST /api/v1/checks/run`

This is an on-demand check runner, not a persistent scheduler. Add authentication, allow-listing/egress controls and a scheduler before exposing it to untrusted users.
