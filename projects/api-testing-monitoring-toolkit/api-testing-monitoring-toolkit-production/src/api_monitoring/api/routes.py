from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, HttpUrl
from api_monitoring.engine.checker import execute_check

router = APIRouter()
class CheckRequest(BaseModel):
    name: str = "Endpoint check"
    url: HttpUrl
    method: str = "GET"
    expected_status: int = Field(default=200, ge=100, le=599)
    headers: dict[str, str] = Field(default_factory=dict)
    json_contains: dict = Field(default_factory=dict)
    timeout_seconds: float = Field(default=5.0, gt=0, le=60)

@router.post("/checks/run")
async def run_check(request: CheckRequest):
    result = await execute_check(request.model_dump(mode="json"), request.timeout_seconds)
    return result
