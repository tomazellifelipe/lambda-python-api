from fastapi import FastAPI
from http import HTTPStatus
from mangum import Mangum

from src.utils.http_response import build_response
from src.v1.routes import router as v1_router

app = FastAPI(
    description="AWS Lambda API with FastAPI",
    docs_url="/docs",
    title="AWS Lambda API with FastAPI",
    version="0.0.1",
)


@app.get("/ping", name="healthcheck", tags=["healthcheck"])
async def healthcheck():
    return build_response(
        http_status=HTTPStatus.OK, body={"message": "Pong, system is online."}
    )


app.include_router(v1_router, prefix="/api/v1")
handler = Mangum(app)
