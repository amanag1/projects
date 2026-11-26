from fastapi.testclient import TestClient
from document_intelligence.main import app

client = TestClient(app)

def test_health_and_ready():
    assert client.get("/health").json() == {"status": "ok"}
    assert client.get("/ready").json() == {"status": "ready"}

def test_extract_text():
    response = client.post("/api/v1/extract", files={"file": ("note.txt", b"hello world", "text/plain")})
    assert response.status_code == 200
    assert response.json()["word_count"] == 2

def test_reject_extension():
    response = client.post("/api/v1/extract", files={"file": ("malware.exe", b"x", "application/octet-stream")})
    assert response.status_code == 415
