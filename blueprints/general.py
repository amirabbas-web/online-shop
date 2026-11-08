from flask import Blueprint, render_template

general = Blueprint("general_blueprint", __name__)

@general.route("/")
def home():
    return render_template("general/main.html")

@general.route("/about")
def about():
    return "about us"