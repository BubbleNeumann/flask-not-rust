from . import main
from flask import render_template
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class SignUpForm(FlaskForm):
    username = StringField('Имя пользователя:', validators=[DataRequired()])
    email = StringField('Почта:', validators=[DataRequired()])
    password = PasswordField('Пароль:', validators=[DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Повторите пароль:', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, field):
        pass

    def validate_email(self, field):
        pass

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', )
    submit = SubmitField('Sign Up')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/text_view')
def browse():
    return render_template('text_view.html')

@main.route('/search')
def search():
    return render_template('search.html')

@main.route('/user')
def user():
    return render_template('user.html')

@main.route('/upload')
def upload():
    return render_template('upload.html')

@main.route('/sign_up')
def sign_up():
    form = SignUpForm()
    return render_template('auth/signup.html', form=form)

@main.route('/login')
def login():
    return render_template('login.html')
