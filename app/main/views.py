from . import main
from flask import render_template
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, field):
        pass

    def validate_email(self, field):
        # TODO write sql query
        pass

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', )
    submit = SubmitField('Sign Up')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/browse')
def browse():
    return render_template('browse.html')

@main.route('/auth/sign_up')
def sign_up():
    form = SignUpForm()
    return render_template('auth/signup.html', form=form)

@main.route('/auth/login')
def login():
    return render_template('auth/login.html')
