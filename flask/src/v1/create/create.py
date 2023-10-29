from flask import Blueprint


router = Blueprint(name="create", import_name=__name__)


@router.route("", methods=["GET"])
def create():
    return {"succes": 200, "message": "something was created"}
