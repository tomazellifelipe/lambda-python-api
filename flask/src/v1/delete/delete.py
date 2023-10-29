from flask import Blueprint


router = Blueprint(name="delete", import_name=__name__)


@router.route("", methods=["GET"])
def delete():
    return {"succes": 200, "message": "something was deleted"}
