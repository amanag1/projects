"""Upload and process a bounded batch of files."""
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZIP_DEFLATED, ZipFile
from fastapi import APIRouter, BackgroundTasks, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from file_automation.core.settings import settings
from file_automation.engine.organizer import organize_directory, write_manifest

router = APIRouter(prefix="/api/v1", tags=["processing"])
CHUNK_SIZE = 1024 * 1024


@router.post("/process", response_class=FileResponse)
async def process_files(background_tasks: BackgroundTasks, files: list[UploadFile] = File(...)):
    if not files:
        raise HTTPException(status_code=400, detail="Upload at least one file")
    if len(files) > settings.max_files_per_batch:
        raise HTTPException(status_code=413, detail="File count limit exceeded")

    workspace = TemporaryDirectory(prefix="file-batch-")
    root = Path(workspace.name)
    incoming = root / "incoming"
    organized = root / "organized"
    incoming.mkdir()
    total_bytes = 0
    seen_names: set[str] = set()

    try:
        for index, upload in enumerate(files, start=1):
            original = Path(upload.filename or f"upload-{index}").name
            if original in {"", ".", ".."}:
                original = f"upload-{index}"
            # Prefix avoids collisions while preserving the readable original name.
            safe_name = f"{index:04d}_{original}"
            if safe_name in seen_names:
                raise HTTPException(status_code=400, detail="Duplicate upload name")
            seen_names.add(safe_name)
            destination = incoming / safe_name
            with destination.open("wb") as output:
                while chunk := await upload.read(CHUNK_SIZE):
                    total_bytes += len(chunk)
                    if total_bytes > settings.max_upload_mb * 1024 * 1024:
                        raise HTTPException(status_code=413, detail="Combined upload size limit exceeded")
                    output.write(chunk)
            await upload.close()

        organize_directory(incoming, organized)
        write_manifest(organized, organized / "manifest.json")
        archive = root / "processed-files.zip"
        with ZipFile(archive, "w", compression=ZIP_DEFLATED) as bundle:
            for item in sorted(organized.rglob("*")):
                if item.is_file():
                    bundle.write(item, item.relative_to(organized))
        background_tasks.add_task(workspace.cleanup)
        return FileResponse(archive, media_type="application/zip",
                            filename="processed-files.zip", background=background_tasks)
    except HTTPException:
        workspace.cleanup()
        raise
    except Exception:
        workspace.cleanup()
        raise
