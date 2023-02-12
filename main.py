from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, SubmitField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, Email

import keys

app = Flask(__name__)
app.config['SECRET_KEY'] = keys.SECRET_KEY
bootstrap = Bootstrap(app)

class SignUpForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    # email = EmailField('Email', validators=[Email()])
    submit = SubmitField('Submit')

# class EmailForm(FlaskForm):
#     name = EmailField('What is your email?', validators=[Email()])
#     submit = SubmitField('Submit')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/auth/sign_up", methods=['GET', 'POST'])
def sign_up():
    name = None
    form = SignUpForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        # email = form.email.data
        # form.name.data = form.email.data = ''
    return render_template('auth/signup.html', form=form, name=name)

@app.route("/auth/login")
def login():
    return render_template('auth/login.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
