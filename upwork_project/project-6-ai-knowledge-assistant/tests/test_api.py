from fastapi.testclient import TestClient
from knowledge_assistant.api import app

client = TestClient(app)

def test_health():
    assert client.get("/health").json() == {"status": "ok"}

def test_answer_returns_sources():
    response = client.post("/answer", json={
        "question": "Who approves leave?",
        "passages": [{"document": "policy.md", "text": "A manager approves leave requests.", "ordinal": 1}]
    })
    assert response.status_code == 200
    payload = response.json()
    assert payload["needs_review"] is False
    assert payload["sources"][0]["document"] == "policy.md"

def test_answer_abstains_without_evidence():
    response = client.post("/answer", json={"question": "Parking policy?", "passages": []})
    assert response.status_code == 200
    assert response.json()["needs_review"] is True
