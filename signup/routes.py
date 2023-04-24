from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from models.models import Person
from extensions import db

signup = Blueprint("signup", __name__, url_prefix="/")


@signup.route("/signup", methods=["GET", "POST"])
def user_signup():
    if request.method == "POST":
        email = request.form["email"]
        name = request.form["name"]
        password = request.form["password"]

        user = Person.query.filter_by(email=email).first()

        if (
            user
        ):  # if user is found, redirect back to signup page so user can try again
            flash("Email address already exists")
            return redirect(url_for("signup.user_signup"))

        new_user = Person(
            email=email,
            name=name,
            password=generate_password_hash(password, method="sha256"),
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("login.user_login"))

    return render_template("signup.html")
