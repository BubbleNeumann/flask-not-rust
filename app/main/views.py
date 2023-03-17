from . import main
from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo

from ..models import User, Text, Tag, Fandom


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


@main.route('/')
def index():
    latest_texts = Text.get_latest(1)
    return render_template('index.html', texts=latest_texts)


@main.route('/text_view/<int:id>')
def text_view(id: int):
    text = Text.get_text_by_id(id=id)
    authors = text.get_authors()
    return render_template('text_view.html', text=text, authors=authors)


@main.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST' and request.form.get('submit') == 'Искать':
        # print(request.form.getlist('tags'))
        texts = Text.get_texts_with_tags(tags=request.form.getlist('tags'))
        return render_template(
            'search_results.html',
            texts=texts
        )

    return render_template(
        'search.html',
        age_restrs=Text.get_age_restrs(),
        tags=Tag.get_all_tags(),
        fandoms=Fandom.get_all_fandoms()
    )


@main.route('/user/<username>')
def user(username):
    user = User.get_user_by_username(username=username)
    texts = user.get_texts()
    return render_template('user.html', user=user, texts=texts)


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
