from flask import Blueprint, redirect, url_for
from flask_login import login_required, logout_user

logout = Blueprint("logout", __name__, url_prefix="/")


@logout.route("/logout", methods=["POST"])
@login_required
def user_logout_session():
    logout_user()
    return redirect(url_for("login.user_login"))
