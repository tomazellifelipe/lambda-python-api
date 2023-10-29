from flask import Blueprint

from src.v1.create import create
from src.v1.read import read
from src.v1.update import update
from src.v1.delete import delete


router = Blueprint(name="api", import_name=__name__ ,url_prefix="/api/v1")
router.register_blueprint(create.router, url_prefix="/create")
router.register_blueprint(read.router, url_prefix="/read")
router.register_blueprint(update.router, url_prefix="/update")
router.register_blueprint(delete.router, url_prefix="/delete")
