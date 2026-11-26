from fastapi.testclient import TestClient
from file_automation.main import app

client = TestClient(app)


def test_health_and_ready():
    assert client.get("/health").json() == {"status": "ok"}
    assert client.get("/ready").json() == {"status": "ready"}


def test_process_returns_zip():
    response = client.post("/api/v1/process", files=[
        ("files", ("notes.txt", b"hello world", "text/plain")),
        ("files", ("report.csv", b"a,b\n1,2\n", "text/csv")),
    ])
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/zip"
    assert response.content[:2] == b"PK"


def test_empty_upload_rejected():
    response = client.post("/api/v1/process", files=[])
    assert response.status_code in (400, 422)
