from flask import Blueprint, render_template

#defining blueprints for accounts related content
accounts = Blueprint('accounts', __name__)


@accounts.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('accounts/register.html')