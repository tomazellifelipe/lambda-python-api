from flask import Blueprint


router = Blueprint(name="read", import_name=__name__)


@router.route("", methods=["GET"])
def read():
    return {"succes": 200, "message": "something was read"}
