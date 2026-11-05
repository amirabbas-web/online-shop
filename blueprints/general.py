from flask import Blueprint

general = Blueprint("general_blueprint", __name__)

@general.route("/")
def home():
    return "this is main page"

@general.route("/about")
def about():
    return "about us"