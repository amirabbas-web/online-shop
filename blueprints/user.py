from flask import Blueprint, render_template, request, redirect, url_for, flash
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
        user = User.query.filter(User.username == username).first()
        if register != None:
            if user != None:
                flash("نام کاربری قبلا انتخاب شده.")
                return redirect(url_for("user_blueprint.home"))
            user = User(username=username, password=sha256_crypt.encrypt(password), phone=phone, address=address)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for("user_blueprint.dashboard"))
        else:
            user = User.query.filter(User.username == username).first()
            if user == None:
                flash("نام کاربری یا رمز عبور اشتباه است")
                return redirect(url_for("user_blueprint.home"))
            if sha256_crypt.verify(password, user.password):
                login_user(user)
                return redirect(url_for('user_blueprint.dashboard'))
            else:
                flash("نام کاربری یا رمز عبور اشتباه است")
                return redirect(url_for("user_blueprint.home"))
@user.route("/dashboard")
def dashboard():
    return "user dashboard"