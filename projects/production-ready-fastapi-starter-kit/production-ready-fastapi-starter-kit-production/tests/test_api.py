from fastapi.testclient import TestClient
from fastapi_service.main import app

client = TestClient(app)


def test_health_and_readiness():
    assert client.get("/health").json() == {"status": "ok"}
    assert client.get("/ready").json() == {"status": "ready"}


def test_greeting_has_request_id():
    response = client.post("/api/v1/greetings", json={"name": "Grace"},
                            headers={"X-Request-ID": "test-request-123"})
    assert response.status_code == 200
    assert response.json()["message"] == "Hello, Grace!"
    assert response.json()["request_id"] == "test-request-123"
    assert response.headers["X-Request-ID"] == "test-request-123"


def test_validation_error():
    assert client.post("/api/v1/greetings", json={"name": ""}).status_code == 422
