import json
from http import HTTPStatus
from typing import Any


def build_response(http_status: HTTPStatus, body: dict[str, Any]) -> dict[str, Any]:
    return {
        "statusCode": http_status,
        "headers": {"Content-Type": "application/json"},
        "body": body,
    }
