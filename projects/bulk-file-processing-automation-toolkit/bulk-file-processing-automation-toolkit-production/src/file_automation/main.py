from fastapi import FastAPI
from file_automation.api.routes import router

app = FastAPI(title="Bulk File Processing API", version="1.0.0")
app.include_router(router)


@app.get("/health", tags=["operations"])
def health():
    return {"status": "ok"}


@app.get("/ready", tags=["operations"])
def ready():
    return {"status": "ready"}
