from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user
from werkzeug.security import check_password_hash
from models.models import Person
from extensions import db

login = Blueprint("login", __name__, url_prefix="")


@login.route("/")
def user_login():
    return render_template("login.html")


@login.route("/", methods=["POST"])
def user_login_post():
    email = request.form.get("email")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False

    user = Person.query.filter_by(email=email).first()

    # check if the user actually exists
    if not user or not check_password_hash(user.password, password):
        flash("Please check your login details and try again.")
        return redirect(
            url_for("login.user_login")
        )  # if the user doesn't exist or password is wrong

    # if passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for("home.homepage"))
