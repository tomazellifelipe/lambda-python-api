import logging
from functools import wraps
from http import HTTPStatus

from pydantic import BaseModel, ValidationError

from flask import request
from src.utils.http_response import build_response


def event_validator(model: BaseModel) -> callable:
    def wrapper(f):
        @wraps(f)
        def validator(*args, **kwargs):
            try:
                event = model(**request.json)
            except ValidationError as e:
                logging.debug("bad request", {"errors": e.errors(), "payload": request.json})
                return (
                    build_response(body={"errors": e.errors()}),
                    HTTPStatus.BAD_REQUEST,
                )
            return f(event, *args, **kwargs)

        return validator

    return wrapper
