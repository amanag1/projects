from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_root_and_health():
    assert client.get("/").status_code == 200
    assert client.get("/health").json() == {"status": "ok"}


def test_greeting():
    response = client.post("/greetings", json={"name": "Ada"})
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Ada!"}


def test_invalid_greeting():
    assert client.post("/greetings", json={"name": ""}).status_code == 422
