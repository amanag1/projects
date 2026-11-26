from fastapi import APIRouter, Request
from fastapi_service.api.schemas import GreetingRequest, GreetingResponse
from fastapi_service.services.greetings import build_greeting

router = APIRouter()


@router.get("/")
def root():
    return {"service": "fastapi-service", "version": "1.0.0"}


@router.post("/greetings", response_model=GreetingResponse)
def create_greeting(payload: GreetingRequest, request: Request):
    return GreetingResponse(
        message=build_greeting(payload.name),
        request_id=getattr(request.state, "request_id", None),
    )
