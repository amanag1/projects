from fastapi import APIRouter, File, HTTPException, UploadFile
from document_intelligence.api.schemas import ExtractionResult
from document_intelligence.core.config import settings
from document_intelligence.services.extraction_service import extract_document

router = APIRouter(prefix="/api/v1", tags=["extraction"])

@router.post("/extract", response_model=ExtractionResult)
async def extract(file: UploadFile = File(...)):
    filename = file.filename or ""
    extension = "." + filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
    if extension not in settings.extension_set:
        raise HTTPException(status_code=415, detail="File extension is not supported")
    content = await file.read(settings.max_upload_bytes + 1)
    if len(content) > settings.max_upload_bytes:
        raise HTTPException(status_code=413, detail="File exceeds configured upload limit")
    if not content:
        raise HTTPException(status_code=422, detail="Uploaded file is empty")
    try:
        return extract_document(filename, content)
    except (UnicodeDecodeError, ValueError) as exc:
        raise HTTPException(status_code=422, detail=f"Could not extract document: {exc}") from exc
    except Exception as exc:
        raise HTTPException(status_code=422, detail="Document could not be parsed") from exc
