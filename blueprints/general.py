from flask import Blueprint

general = Blueprint("general_blueprint", __name__)

@general.route("/")
def hello_world():
    return "Hello World!"