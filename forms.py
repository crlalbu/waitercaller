from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms.fields.html5 import EmailField
from wtforms import validators


class RegistrationForm(FlaskForm):
    email = EmailField('email', validators=[validators.DataRequired(), validators.Email()])

    password = PasswordField('password', validators=[validators.DataRequired(),
    validators.Length(min=6, message="password must be greater than 6 characters")])

    password2 = PasswordField('password2',
    validators=[validators.DataRequired(),
    validators.EqualTo('password', message='Password must match')])

    submit = SubmitField('submit', [validators.DataRequired()])