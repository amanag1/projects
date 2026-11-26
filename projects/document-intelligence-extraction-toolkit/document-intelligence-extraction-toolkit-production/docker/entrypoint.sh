#!/bin/sh
set -eu
exec uvicorn document_intelligence.main:app --host 0.0.0.0 --port 8000
