import logging
from http import HTTPStatus

from flask import Blueprint, Response, request
from src.utils.http_response import build_response
from src.utils.parser import parse_and_validate
from src.v1.models import Item

router = Blueprint(name="api", import_name=__name__, url_prefix="/api/v1")


@router.route("/create", methods=["POST"])
def create() -> tuple[Response, int]:
    event: Item = parse_and_validate(request.json)
    message: str = (
        f"item {event.name} was created with price R${event.price:.2f}"
    )
    logging.debug("Item created", event.model_dump())
    return build_response(body={"message": message}), HTTPStatus.OK
