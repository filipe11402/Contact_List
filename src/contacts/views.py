from flask import Blueprint


contacts = Blueprint('contacts', __name__)

@contacts.route('/main', methods=['GET'])
def index():
    return '<h1>main page</h1>'