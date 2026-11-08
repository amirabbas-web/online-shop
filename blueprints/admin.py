from flask import Blueprint, render_template, request, session, redirect, url_for, abort
from config import *
from extensions import *
from models.Product import Product
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
    return render_template("admin/dashboard.html")


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

        p = Product(name=name, description=description, price=price)
        if active == None:
            p.active = 0
        else:
            p.active = 1
        db.session.add(p)
        db.session.commit()

        return "done"