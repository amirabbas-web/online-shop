from flask import Blueprint, render_template, request, session, redirect, url_for, abort
from config import *
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


@admin.route("/dashboard/products")
def products():
    return "this is products page"