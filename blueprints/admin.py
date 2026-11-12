from flask import Blueprint, render_template, request, session, redirect, url_for, abort
from config import *
from extensions import *
from models.Product import Product
from models.Cart import Cart

admin = Blueprint("admin_blueprint", __name__, url_prefix="/admin")

@admin.before_request
def before_request():
    if session.get("admin_login") == None and request.endpoint != "admin_blueprint.login":
        abort(403)


@admin.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("admin/login.html")
    else:
        username = request.form.get("user", None)
        password = request.form.get("pass", None)

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["admin_login"] = username
            return redirect(url_for("admin_blueprint.dashboard"))
        else:
            return redirect(url_for("admin_blueprint.login"))


@admin.route("/dashboard")
def dashboard():
    carts = Cart.query.filter(Cart.status != "pending").all()
    return render_template("admin/dashboard.html", carts=carts)

@admin.route("/dashboard/order/<id>", methods=["GET", "POST"])
def order(id):
    cart = Cart.query.filter(Cart.id == id).first_or_404()
    if request.method == "GET":
        return render_template("admin/order.html", cart=cart)
    else:
        status = request.form.get("status")
        cart.status = status
        db.session.commit()
        return redirect(url_for("admin_blueprint.order", id=id))

@admin.route("/dashboard/products", methods=["GET", "POST"])
def products():
    if request.method == "GET":
        products = Product.query.all()
        return render_template("admin/product.html", products=products)
    else:
        name = request.form.get("name", None)
        description = request.form.get("description", None)
        price = request.form.get("price", None)
        active = request.form.get("active", None)
        file = request.files.get("cover", None)
        p = Product(name=name, description=description, price=price)
        if active == None:
            p.active = 0
        else:
            p.active = 1
        db.session.add(p)
        db.session.commit()
        file.save(f'static/cover/{p.id}.jpg')

        return "done"

@admin.route("/dashboard/edit-product/<id>", methods=["GET", "POST"])
def edit_product(id):
    product = Product.query.filter(Product.id == id).first_or_404()
    if request.method == "GET":
        return render_template("admin/edit-product.html", product=product)
    else:
        name = request.form.get("name", None)
        description = request.form.get("description", None)
        price = request.form.get("price", None)
        active = request.form.get("active", None)
        file = request.files.get("cover", None)
        product.name = name
        product.description = description
        product.price = price
        if active == None:
            product.active = 0
        else:
            product.active = 1

        if file and file.filename:
            file.save(f'static/cover/{product.id}.jpg')
        db.session.commit()

        return redirect(url_for("admin_blueprint.products"))