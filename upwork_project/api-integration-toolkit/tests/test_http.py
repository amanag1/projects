import httpx
import pytest
from api_integration.http import IntegrationHTTPError, send_json

def test_sends_idempotency_header_and_parses_json():
    def handler(request):
        assert request.headers["Idempotency-Key"] == "key-1"
        return httpx.Response(200, json={"accepted": True})
    result = send_json("https://example.test", "/records", {"id": 1},
                       idempotency_key="key-1", transport=httpx.MockTransport(handler))
    assert result == {"accepted": True}

def test_requires_idempotency_key():
    with pytest.raises(ValueError):
        send_json("https://example.test", "/records", {}, idempotency_key=" ")

def test_non_retryable_client_error_is_reported():
    def handler(request):
        return httpx.Response(400, json={"error": "bad request"})
    with pytest.raises(IntegrationHTTPError, match="HTTP 400"):
        send_json("https://example.test", "/records", {}, idempotency_key="k",
                  transport=httpx.MockTransport(handler))
