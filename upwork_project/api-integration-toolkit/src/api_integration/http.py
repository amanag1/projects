"""HTTP transport with bounded retries and explicit idempotency support."""
from __future__ import annotations
import time
from typing import Any
import httpx

RETRYABLE_STATUS = {408, 425, 429, 500, 502, 503, 504}

class IntegrationHTTPError(RuntimeError):
    pass

def send_json(base_url: str, path: str, payload: dict[str, Any], *,
              idempotency_key: str, token: str | None = None,
              max_attempts: int = 3, timeout: float = 20.0,
              transport: httpx.BaseTransport | None = None) -> dict[str, Any]:
    if not idempotency_key.strip():
        raise ValueError("idempotency_key is required for write requests")
    if max_attempts < 1 or max_attempts > 6:
        raise ValueError("max_attempts must be between 1 and 6")
    headers = {"Idempotency-Key": idempotency_key, "Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    last_error = "unknown error"
    with httpx.Client(base_url=base_url, timeout=timeout, transport=transport) as client:
        for attempt in range(max_attempts):
            try:
                response = client.post(path, json=payload, headers=headers)
                if response.status_code in RETRYABLE_STATUS:
                    last_error = f"retryable HTTP {response.status_code}"
                    if attempt + 1 < max_attempts:
                        time.sleep(min(0.25 * (2 ** attempt), 2.0))
                        continue
                response.raise_for_status()
                if not response.content:
                    return {}
                try:
                    return response.json()
                except ValueError as exc:
                    raise IntegrationHTTPError("Target returned non-JSON success response") from exc
            except (httpx.TimeoutException, httpx.NetworkError) as exc:
                last_error = type(exc).__name__
                if attempt + 1 < max_attempts:
                    time.sleep(min(0.25 * (2 ** attempt), 2.0))
                    continue
                raise IntegrationHTTPError(f"Request failed after {max_attempts} attempts: {last_error}") from exc
            except httpx.HTTPStatusError as exc:
                raise IntegrationHTTPError(f"Target rejected request: HTTP {exc.response.status_code}") from exc
    raise IntegrationHTTPError(f"Request failed after {max_attempts} attempts: {last_error}")
