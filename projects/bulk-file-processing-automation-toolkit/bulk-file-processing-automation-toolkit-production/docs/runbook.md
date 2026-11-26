# Runbook

## Health checks
Use `GET /health` for process health and `GET /ready` for readiness.

## Common issues
- **413 response:** reduce total upload size or file count.
- **5xx response:** inspect application logs and verify writable temporary storage.
- **Archive download interrupted:** retry the request; each request is independent.

## Security
Keep the service behind a trusted gateway. Add authentication, rate limiting, malware scanning, request timeouts and storage quotas before public exposure. Monitor temporary disk usage and worker memory.
