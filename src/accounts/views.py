from flask import Blueprint, render_template, request, flash, url_for, redirect
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from src import db


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
            flash("Email already beeing used", category='error')
        elif len(first_name) < 4 or len(last_name) < 4:
            flash("Too short, should be bigger than 4", category='error')
        elif password1 != password2:
            flash("Passwords dont match", category='error')
        else:
            new_user = User(email=email, first_name=first_name, last_name=last_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("User created successfuly", category='success')
            return redirect(url_for('accounts.login'))

    return render_template('accounts/register.html')


@accounts.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('accounts/login.html')
