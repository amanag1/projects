# Reliable API Integration Toolkit

A reusable integration pattern for moving records between business systems without treating a successful HTTP response as proof that the data is correct.

## Problem
Manual copy/paste between SaaS tools, spreadsheets and internal systems wastes time and introduces mismatches, duplicates and silent failures.

## Included design
- Explicit source/target contracts and field mapping.
- Pre-flight validation before any write.
- Dry-run mode that previews intended changes.
- Bounded retries for transient failures with exponential backoff.
- Idempotency keys to reduce duplicate writes.
- Structured per-record outcomes and a reconciliation report.
- Secrets supplied through environment variables, never committed.
- Human approval gate for destructive or externally visible operations.

## Why this is more than an AI-generated API script
The integration is treated as a controlled data workflow: validate, preview, execute, reconcile and audit. The operator can see what will change, what failed, what was retried and what needs manual attention.

## Starter implementation
The first module provides deterministic validation, mapping, idempotency and dry-run planning without binding to a particular vendor. Add provider adapters only after the client's API contract and authentication method are confirmed.

## Run tests
```bash
python -m pip install -e ".[dev]"
pytest -q
```
