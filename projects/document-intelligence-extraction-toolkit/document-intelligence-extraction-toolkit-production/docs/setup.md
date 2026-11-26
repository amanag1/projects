# Setup

Requires Python 3.11+ and pip. Install with `pip install -e ".[dev]"`, then run `uvicorn document_intelligence.main:app --reload` from this directory. Configure upload size and accepted extensions through environment variables. For containers, copy `.env.example` to `.env` and run `docker compose up --build`.
