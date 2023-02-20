import os
from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, SubmitField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, Email
# from flask_sqlalchemy import SQLAlchemy

import keys

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = keys.SECRET_KEY
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap(app)
# db = SQLAlchemy(app)

class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')


# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True)
#     email = db.Column(db.String(64), unique=True, index=True)
#
#     def __repr__(self):
#         # return '<User %r>' %self.username
#         return f'User {self.id} {self.username} {self.email}'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/browse")
def browse():
    return render_template('browse.html')

@app.route("/auth/sign_up", methods=['GET', 'POST'])
def sign_up():
    # if session['known']:
    #     return redirect(url_for('index'))
    form = SignUpForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(username=form.username.data).first()
    #     if user is None:
    #         user = User(username=form.username.data, email=form.email.data)
    #         db.session.add(user)
    #         db.session.commit()
    #         session['known'] = False
    #     else:
    #         session['known'] = True
    #     session['username'] = form.username.data
    #     session['email'] = form.email.data
    #     form.username.data = form.email.data = ''
    #     return redirect(url_for('index'))
    return render_template('auth/signup.html', form=form,
                           username=session.get('username'), known=session.get('known', False))

@app.route("/auth/login")
def login():
    return render_template('auth/login.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
