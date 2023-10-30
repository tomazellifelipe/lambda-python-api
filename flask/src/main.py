from http import HTTPStatus

from src.utils import logger
from src.utils.http_response import build_response
from src.v1.routes import router as v1_router

from flask import Flask

logger.load()
app = Flask(__name__)
app.register_blueprint(v1_router)


@app.route("/ping", methods=["GET"])
def healthcheck():
    return build_response(
        http_status=HTTPStatus.OK, body={"message": "Pong, system is online"}
    )
