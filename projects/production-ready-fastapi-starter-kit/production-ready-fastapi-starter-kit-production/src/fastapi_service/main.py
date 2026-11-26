from fastapi import FastAPI
from fastapi_service.api.routes import router
from fastapi_service.core.config import settings
from fastapi_service.core.logging import configure_logging
from fastapi_service.core.middleware import RequestContextMiddleware

configure_logging()
app = FastAPI(title=settings.app_name, version="1.0.0")
app.add_middleware(RequestContextMiddleware)
app.include_router(router, prefix=settings.api_prefix)


@app.get("/health", tags=["operations"])
def health():
    return {"status": "ok"}


@app.get("/ready", tags=["operations"])
def ready():
    return {"status": "ready"}
