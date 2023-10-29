from flask import Blueprint, request
from http import HTTPStatus
from pydantic import ValidationError

from src.utils.http_response import build_response
from src.v1.schemas.item import Item

router = Blueprint(name="create", import_name=__name__)


@router.route("", methods=["POST"])
def create():
    try:
        item = Item(**request.json)
    except ValidationError as e:
        return build_response(
            http_status=HTTPStatus.BAD_REQUEST,
            body={"message": "bad request", "errors": e.errors()},
        )
    message = f"item {item.name} was created with price R${item.price:.2f}"
    return build_response(http_status=HTTPStatus.OK, body={"message": message})
