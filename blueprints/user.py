from flask import Blueprint
from models.User import User
from models.Product import Product

user = Blueprint("user_blueprint", __name__, url_prefix="/user")

@user.route("/")
def home():
    return "this is user page"