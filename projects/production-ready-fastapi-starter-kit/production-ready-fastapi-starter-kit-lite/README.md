# FastAPI Starter Kit — Lite

A compact FastAPI starter for small services and learning. It includes environment configuration, health checks, request validation, a predictable error response and pytest coverage.

## Requirements
Python 3.10+.

## Setup
```bash
python -m venv .venv
# Activate the environment
pip install -r requirements.txt
uvicorn app:app --reload
```
Open `http://127.0.0.1:8000/docs`.

## Endpoints
- `GET /`: service information
- `GET /health`: process health
- `POST /greetings`: validate and return a greeting

## Tests
```bash
pytest -q
```
