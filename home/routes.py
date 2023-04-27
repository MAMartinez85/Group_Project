from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models.models import Event

home = Blueprint("home", __name__, url_prefix="")

@home.route("/home", methods=['GET'])
@login_required
def homepage():
    events = Event.query.all()
    return render_template('homepage.html', events=events)
