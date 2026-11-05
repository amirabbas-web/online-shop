from flask import Blueprint

admin = Blueprint("admin_blueprint", __name__, url_prefix="/admin")

@admin.route("/")
def home():
    return "this is admin page"