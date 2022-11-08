from werkzeug.security import generate_password_hash

from flask import render_template, redirect, url_for, flash
from flask_login import login_user

from app.models import UserData, UserModel
from app.forms import LoginForm

from app.helpers.users import get_user_by_key, create_user

from . import users

@users.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_form = LoginForm()

    context = {
        'signup_form': signup_form
    }

    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data

        user_item = get_user_by_key(username)

        if "Item" not in user_item:
            password_hash = generate_password_hash(password)
            user_data = UserData(username, password_hash)

            create_user(user_data)

            user = UserModel(user_data)
            login_user(user)

            flash('Successfully')

            return redirect(url_for('home'))

        else:
            flash('User already exists')

    return render_template('signup.html', **context)