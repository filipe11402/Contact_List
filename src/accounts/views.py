from flask import Blueprint

#defining blueprints for accounts related content
accounts = Blueprint('accounts', __name__)


@accounts.route('/register', methods=['GET', 'POST'])
def register():
    return '<h1>teste</h1>'