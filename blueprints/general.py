from flask import Blueprint, render_template
from models.Product import Product
general = Blueprint("general_blueprint", __name__)

@general.route("/")
def home():
    products = Product.query.filter(Product.active == 1).all()
    return render_template("general/main.html", products=products)

@general.route("/product/<int:id>/<string:name>")
def product(id, name):
    product_do = Product.query.filter(Product.id == id).filter(Product.name == name).filter(Product.active == 1).first_or_404()
    return render_template("general/product.html", p=product_do)

@general.route("/about")
def about():
    return render_template("general/about.html")