# Operations runbook

## Health checks
- `GET /health`: process liveness.
- `GET /ready`: basic readiness response.

## Common issues
- 413: reduce file size or adjust `MAX_UPLOAD_BYTES`.
- 415: extension is not in `ALLOWED_EXTENSIONS`.
- 422: file is malformed, encrypted, unsupported encoding or cannot be parsed.
- Empty PDF text: likely scanned/image-only content; OCR is not included.

## Operations
Monitor request rates, response codes, latency and memory. Keep upload limits conservative. Place authentication, rate limiting and network restrictions at the gateway. Do not log document contents or credentials.
