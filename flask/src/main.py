from http import HTTPStatus

from flask import Flask, Response
from src.utils import logger
from src.utils.http_response import build_response
from src.v1.routes import router as v1_router

logger.load()
app = Flask(__name__)
app.register_blueprint(v1_router)


@app.route("/health-check/alive", methods=["GET"])
def alive() -> tuple[Response, int]:
    return (
        build_response(body={"message": "Pong, system is online"}),
        HTTPStatus.OK,
    )
