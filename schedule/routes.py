from flask import Blueprint, render_template, redirect, url_for, flash, request
from extensions import db
from models.models import Event

schedule = Blueprint("schedule", name, url_prefix="")


@schedule.route("/schedule", methods=["GET", "POST"])
def schedule_creator():
    events = Event.query.all()
    if request.method == "POST":
        title = request.form["title"]
        start_time = (
            request.form["start_date"]
            + " "
            + request.form["start_hour"]
            + ":"
            + request.form["start_minute"]
            + ":00"
        )
        end_time = (
            request.form["end_date"]
            + " "
            + request.form["end_hour"]
            + ":"
            + request.form["end_minute"]
            + ":00"
        )
        event = Event(title=title, start_time=start_time, end_time=end_time)
        db.session.add(event)
        db.session.commit()
        flash("Event added successfully.")
        return redirect(url_for("schedule.schedule_creator"))
    return render_template("schedule.html", events=events)


@schedule.route("/event/<int:event_id>/edit", methods=["GET", "POST"])
def edit_event(event_id):
    event = Event.query.get_or_404(event_id)
    if request.method == "POST":
        event.title = request.form["title"]
        event.start_time = (
            request.form["start_date"]
            + " "
            + request.form["start_hour"]
            + ":"
            + request.form["start_minute"]
            + ":00"
        )
        event.end_time = (
            request.form["end_date"]
            + " "
            + request.form["end_hour"]
            + ":"
            + request.form["end_minute"]
            + ":00"
        )
        db.session.commit()
        flash("Event updated successfully.")
        return redirect(url_for("schedule"))
    return render_template("edit_event.html", event=event)


@schedule.route("/event/<int:event_id>/delete", methods=["POST"])
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    flash("Event deleted successfully.")
    return redirect(url_for("schedule.schedule_creator"))
