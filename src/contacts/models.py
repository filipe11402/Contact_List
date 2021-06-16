from src import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    phone_number = db.Column(db.Integer)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
