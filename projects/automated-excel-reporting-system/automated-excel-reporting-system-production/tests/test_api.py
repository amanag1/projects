from fastapi.testclient import TestClient
from excel_reporting.main import app

client = TestClient(app)

def test_health():
    assert client.get("/health").json() == {"status": "ok"}

def test_rejects_non_excel_upload():
    response = client.post("/api/v1/reports/profile", files={"file": ("notes.txt", b"hello", "text/plain")})
    assert response.status_code == 415
