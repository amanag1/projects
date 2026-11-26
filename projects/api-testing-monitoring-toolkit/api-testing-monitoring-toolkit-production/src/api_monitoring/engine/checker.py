import time
import httpx

async def execute_check(check: dict, timeout: float = 5.0) -> dict:
    started = time.perf_counter()
    try:
        async with httpx.AsyncClient(timeout=timeout, follow_redirects=True) as client:
            response = await client.request(check.get("method", "GET"), check["url"],
                                            headers=check.get("headers", {}))
        expected = int(check.get("expected_status", 200))
        passed = response.status_code == expected
        expected_json = check.get("json_contains")
        if expected_json:
            try:
                payload = response.json()
                passed = passed and all(payload.get(k) == v for k, v in expected_json.items())
            except (ValueError, AttributeError):
                passed = False
        return {"name": check.get("name", check["url"]), "passed": passed,
                "status": response.status_code, "expected_status": expected,
                "duration_ms": round((time.perf_counter()-started)*1000, 2)}
    except httpx.HTTPError as exc:
        return {"name": check.get("name", check["url"]), "passed": False,
                "error": str(exc), "duration_ms": round((time.perf_counter()-started)*1000, 2)}
