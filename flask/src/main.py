from flask import Flask

from src.v1.routes import router as v1_router

app = Flask(__name__)
app.register_blueprint(v1_router)


@app.route("/ping", methods=["GET"])
def healthcheck():
    return {"success": 200}
