from flask import Blueprint
from http import HTTPStatus

from src.utils.http_response import build_response

router = Blueprint(name="create", import_name=__name__)


@router.route("", methods=["GET"])
def create():
    return build_response(http_status=HTTPStatus.OK, body={"message": "something was created"})
