# Setup

Python 3.10+.

```bash
python -m venv .venv
pip install -e ".[test]"
uvicorn api_monitoring.main:app --app-dir src --reload
pytest -q
```

Use `docker compose up --build` for a container run. The API listens on port 8000.
