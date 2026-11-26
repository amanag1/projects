from pydantic import BaseModel, Field

class ExtractionResult(BaseModel):
    filename: str
    extension: str
    size_bytes: int = Field(ge=0)
    character_count: int = Field(ge=0)
    word_count: int = Field(ge=0)
    page_count: int | None = None
    headings: list[str]
    emails: list[str]
    urls: list[str]
    text: str
