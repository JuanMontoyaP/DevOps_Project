import os
from pymongo import MongoClient

from flask import Flask 
from flask import request, make_response, redirect
from flask import render_template

from flask_bootstrap import Bootstrap

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.flask_db
tasks = db.tasks

bootstrap = Bootstrap(app)

# tasks = ["Finish Flask App", "Set Database", "Jenkins pipeline"]

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')

    tasks.insert_one({'task': 'task_1'})

    context = {
        'user_ip': user_ip,
        'tasks': tasks.find()
    }

    return render_template('home.html', **context)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, host='0.0.0.0', port=port)