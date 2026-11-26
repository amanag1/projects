# Architecture

The FastAPI layer validates a check request and passes it to an asynchronous HTTPX-based checker. The checker enforces a caller-supplied bounded timeout, compares the response status and optionally validates selected JSON fields. It returns a compact result with elapsed milliseconds.

The service runs checks on demand and stores no history. A scheduled monitoring product would need a scheduler, durable result store, alert delivery and tenant-aware access controls. Network egress must be restricted to prevent server-side request forgery.
