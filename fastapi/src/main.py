from fastapi import FastAPI
from mangum import Mangum

from src.v1.routes import router as v1_router

app = FastAPI(
    description="AWS Lambda API with FastAPI",
    docs_url="/docs",
    title="AWS Lambda API with FastAPI",
    version="0.0.1"
)


@app.get("/ping", name="healthcheck", tags=["healthcheck"])
async def healthcheck():
    return {"success": 200}

app.include_router(v1_router, prefix="/api/v1")
handler = Mangum(app)
