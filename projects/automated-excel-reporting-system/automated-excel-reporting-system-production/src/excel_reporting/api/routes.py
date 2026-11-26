from pathlib import Path
from tempfile import TemporaryDirectory
from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from excel_reporting.engine.profiler import build_profile

router = APIRouter()

@router.post("/reports/profile")
async def create_profile(file: UploadFile = File(...)):
    if not file.filename or Path(file.filename).suffix.lower() not in {".xlsx", ".xlsm"}:
        raise HTTPException(status_code=415, detail="Upload an .xlsx or .xlsm workbook")
    temp = TemporaryDirectory()
    source = Path(temp.name) / "source.xlsx"
    output = Path(temp.name) / "profiled_report.xlsx"
    try:
        source.write_bytes(await file.read())
        metadata = build_profile(source, output)
        return FileResponse(output, filename="profiled_report.xlsx",
                            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            background=None)
    except Exception as exc:
        temp.cleanup()
        raise HTTPException(status_code=400, detail=f"Unable to process workbook: {exc}") from exc
