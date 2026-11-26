# Runbook

## Health
- `GET /health`: process health
- `GET /ready`: basic readiness response

These endpoints are intentionally lightweight and do not validate external dependencies because none are configured.

## Troubleshooting
- **Import error:** reinstall with `pip install -e .` and confirm `src` package discovery.
- **Configuration ignored:** check environment variable names and the working directory containing `.env`.
- **Unexpected request IDs:** inspect gateway header forwarding and avoid trusting arbitrary client IDs in security-sensitive audit workflows.

Before production use, add dependency-aware readiness, metrics, tracing, alerting, rate limits and security controls.
