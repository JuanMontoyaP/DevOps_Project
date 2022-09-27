from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Send')

class TaskForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('create')

class DeleteTaskForm(FlaskForm):
    submit = SubmitField('delete')