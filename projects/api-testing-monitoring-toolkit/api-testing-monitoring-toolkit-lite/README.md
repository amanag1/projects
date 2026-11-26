# API Testing & Monitoring Toolkit — Lite

A dependency-free command-line checker for HTTP endpoints. Define checks in JSON, set expected status codes and optionally assert selected JSON response fields. Each result includes pass/fail and elapsed time.

```bash
python app.py sample_data/checks.json --timeout 5
```

Uses only the Python standard library. The sample check requires internet access; tests run against a local HTTP server.
