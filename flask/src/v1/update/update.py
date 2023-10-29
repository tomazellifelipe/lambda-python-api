from flask import Blueprint


router = Blueprint(name="update", import_name=__name__)


@router.route("", methods=["GET"])
def update():
    return {"succes": 200, "message": "something was updated"}
