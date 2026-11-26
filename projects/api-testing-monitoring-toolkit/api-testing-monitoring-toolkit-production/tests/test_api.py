from fastapi.testclient import TestClient
from api_monitoring.main import app
client = TestClient(app)
def test_health():
    assert client.get("/health").json()["status"] == "ok"
def test_check_rejects_invalid_url():
    response = client.post("/api/v1/checks/run", json={"url": "not-a-url"})
    assert response.status_code == 422
