"""Configuration-driven HTTP endpoint checks."""
import json
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

def run_check(check: dict, timeout: float = 5.0) -> dict:
    url = check["url"]
    method = check.get("method", "GET").upper()
    started = time.perf_counter()
    request = Request(url, method=method, headers=check.get("headers", {}))
    try:
        with urlopen(request, timeout=timeout) as response:
            body = response.read()
            status = response.status
    except HTTPError as exc:
        body, status = exc.read(), exc.code
    except (URLError, TimeoutError) as exc:
        return {"name": check.get("name", url), "passed": False, "error": str(exc),
                "duration_ms": round((time.perf_counter()-started)*1000, 2)}
    expected = int(check.get("expected_status", 200))
    passed = status == expected
    expected_json = check.get("json_contains")
    if expected_json:
        try:
            payload = json.loads(body.decode("utf-8"))
            passed = passed and all(payload.get(k) == v for k, v in expected_json.items())
        except (ValueError, AttributeError):
            passed = False
    return {"name": check.get("name", url), "passed": passed, "status": status,
            "expected_status": expected, "duration_ms": round((time.perf_counter()-started)*1000, 2)}
