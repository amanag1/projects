from pydantic import BaseModel, Field


class GreetingRequest(BaseModel):
    name: str = Field(min_length=1, max_length=80)


class GreetingResponse(BaseModel):
    message: str
    request_id: str | None = None
