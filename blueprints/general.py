from flask import Blueprint, render_template
from models.Product import Product
general = Blueprint("general_blueprint", __name__)

@general.route("/")
def home():
    products = Product.query.all()
    return render_template("general/main.html", products=products)

@general.route("/about")
def about():
    return render_template("general/about.html")