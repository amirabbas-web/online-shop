from flask import Blueprint

admin = Blueprint("admin_blueprint", __name__)

@admin.route("/")
def home():
    return "this is main page"