from typing import Any

from flask import Response, make_response


def build_response(body: dict[str, Any]) -> Response:
    response = make_response(body)
    response.headers["Content-Type"] = "application/json"
    return response
