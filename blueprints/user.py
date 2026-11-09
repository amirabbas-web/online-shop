from flask import Blueprint, render_template, request, redirect, url_for
from models.User import *
from flask_login import login_user
from extensions import *
from models.Product import Product
from passlib.hash import sha256_crypt
user = Blueprint("user_blueprint", __name__, url_prefix="/user")

@user.route("/login", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("user/login.html")
    else:
        username = request.form.get('user', None)
        password = request.form.get('pass', None)
        phone = request.form.get('phone', None)
        address = request.form.get('address', None)
        register = request.form.get('register', None)

        if register != None:
            user = User(username=username, password=sha256_crypt.encrypt(password), phone=phone, address=address)
            db.session.add(user)
            db.session.commit()
            login_user(user)
        return redirect(url_for("user_blueprint.dashboard"))

@user.route("/dashboard")
def dashboard():
    return "user dashboard"