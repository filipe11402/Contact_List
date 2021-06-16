from flask import Blueprint, render_template, request
from .models import User


#defining blueprints for accounts related content
accounts = Blueprint('accounts', __name__)


@accounts.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user_check = User.query.filter_by(email=email).first()
        if user_check:
            print("EXISTS")
        else:
            print("DOESNT EXIST")

    return render_template('accounts/register.html')


@accounts.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('accounts/login.html')
