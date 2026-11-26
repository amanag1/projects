from fastapi import FastAPI
from document_intelligence.api.routes import router
from document_intelligence.core.config import settings
from document_intelligence.core.logging_config import configure_logging
from document_intelligence.core.request_id import RequestIdMiddleware

configure_logging()
app = FastAPI(title=settings.app_name, version="1.0.0")
app.add_middleware(RequestIdMiddleware)
app.include_router(router)

@app.get("/health", tags=["operations"])
def health():
    return {"status": "ok"}

@app.get("/ready", tags=["operations"])
def ready():
    return {"status": "ready"}
