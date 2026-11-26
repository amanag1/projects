"""Minimal FastAPI starter application."""
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
try:
    from .engine import greeting
except ImportError:
    from engine import greeting

app = FastAPI(title="FastAPI Starter — Lite", version="1.0.0")


class GreetingRequest(BaseModel):
    name: str = Field(min_length=1, max_length=80)


@app.get("/")
def root():
    return {"service": os.getenv("APP_NAME", "fastapi-lite"), "version": "1.0.0"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/greetings")
def create_greeting(payload: GreetingRequest):
    try:
        return {"message": greeting(payload.name)}
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
