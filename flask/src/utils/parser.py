import logging
from typing import Any

from pydantic import BaseModel, ValidationError


def parse_and_validate(payload: dict[str, Any], model: BaseModel) -> BaseModel:
    try:
        event = model(**payload)
    except:
        logging.debug("Errors", payload)
        raise ValidationError
    return event
