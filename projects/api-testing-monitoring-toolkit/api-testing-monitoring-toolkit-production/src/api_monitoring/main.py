from fastapi import FastAPI
from api_monitoring.api.routes import router
app = FastAPI(title="API Testing & Monitoring Toolkit", version="1.0.0")
app.include_router(router, prefix="/api/v1")
@app.get("/health")
def health():
    return {"status": "ok"}
@app.get("/ready")
def ready():
    return {"status": "ready"}
