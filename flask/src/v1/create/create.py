from functools import wraps
import logging
from http import HTTPStatus

from pydantic import ValidationError
from src.utils.http_response import build_response
from src.v1.schemas.item import Item

from flask import Blueprint, request

router = Blueprint(name="create", import_name=__name__)


def event_validator(model):
    def wrapper(f):
        @wraps(f)
        def validator(*args, **kwargs):
            try:
                _ = model(**request.json)
            except ValidationError as e:
                logging.debug("bad request", e.errors()[0])
                return build_response(
                    http_status=HTTPStatus.BAD_REQUEST,
                    body={"message": "bad request", "errors": e.errors()},
                ), 400
            return f(*args, **kwargs)
        return validator
    return wrapper


@router.route("", methods=["POST"])
@event_validator(model=Item)
def create():
    item = Item(**request.json)
    message = f"item {item.name} was created with price R${item.price:.2f}"
    logging.debug('Item created', item.model_dump())
    return build_response(http_status=HTTPStatus.OK, body={"message": message}), 200
