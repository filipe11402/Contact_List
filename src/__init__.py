from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'filipe'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .accounts.views import accounts
    from .contacts.views import contacts

    app.register_blueprint(accounts, url_prefix='/accounts')
    app.register_blueprint(contacts, url_prefix='/contacts')

    create_database(app)

    return app


def create_database(app):
    if not path.exists('src/' + DB_NAME):
        db.create_all(app=app)
        print("DATABASE CREATED")
