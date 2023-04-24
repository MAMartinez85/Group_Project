from flask import Blueprint, render_template
from flask_login import login_required, current_user

home = Blueprint("home", __name__, url_prefix="")

@home.route("/home")
@login_required
def homepage():
    return render_template('homepage.html')
