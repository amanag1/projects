"""Optional FastAPI interface for the evidence retrieval core."""
from __future__ import annotations
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from .core import Passage, answer_from_evidence

app = FastAPI(title="Knowledge Assistant API", version="0.1.0")

class PassageInput(BaseModel):
    document: str
    text: str
    ordinal: int = Field(ge=1)

class QuestionRequest(BaseModel):
    question: str = Field(min_length=1, max_length=2000)
    passages: list[PassageInput] = Field(default_factory=list, max_length=500)

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/answer")
def answer(request: QuestionRequest) -> dict:
    try:
        result = answer_from_evidence(
            request.question,
            [Passage(p.document, p.text, p.ordinal) for p in request.passages],
        )
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    return {
        "answer": result.answer,
        "needs_review": result.needs_review,
        "sources": [{"document": p.document, "ordinal": p.ordinal, "text": p.text}
                    for p in result.sources],
    }
