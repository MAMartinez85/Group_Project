from extensions import db
from flask_login import UserMixin

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

class Person(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(1000), nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_comment = db.Column(db.String(255), nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    movie_id = db.Column(db.Integer, nullable=False)