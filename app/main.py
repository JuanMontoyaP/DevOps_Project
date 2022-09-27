import os
import unittest

from flask import request, make_response, redirect, session
from flask import render_template

from flask_login import login_required, current_user

from app import create_app

from app import db

app = create_app()


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/home'))
    session['user_ip'] = user_ip

    return response

@app.route('/home', methods=['GET'])
@login_required
def home():
    user_ip = session.get('user_ip')
    username = current_user.id

    context = {
        'user_ip': user_ip,
        'tasks': db.get_task(),
        'username': username
    }

    return render_template('home.html', **context)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)