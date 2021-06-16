from flask_login import UserMixin
from src import db
from src.contacts.models import Contact


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    password = db.Column(db.Integer)
    contacts = db.relationship('Contact')
