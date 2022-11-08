import os
import unittest

from flask import request, make_response, redirect, session, url_for, render_template
from flask_login import login_required, current_user

from app import create_app

from app.forms import TaskForm, DeleteTaskForm
from app.helpers import tasks

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

@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    user_ip = session.get('user_ip')
    username = current_user.id
    task_form = TaskForm()
    delete_from = DeleteTaskForm()

    context = {
        'user_ip': user_ip,
        'tasks': tasks.get_tasks(username),
        'username': username,
        'task_form': task_form,
        'delete_form': delete_from
    }

    if task_form.validate_on_submit():
        tasks.create_task(username, task_form.description.data)

        return redirect(url_for('home'))

    return render_template('home.html', **context)

@app.route('/task/delete/<task_id>', methods=['POST'])
def delete_task(task_id):
    username = current_user.id
    tasks.delete_a_task(username, task_id)

    return redirect(url_for('home'))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)