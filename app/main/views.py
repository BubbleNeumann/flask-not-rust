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


@main.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and request.form.get('submit') == 'Добавить':
        tags = request.form.get('tags')
        new_text.title = request.form.get('title')
        new_text.descr = request.form.get('descr')
        new_text.age_restr = request.form.get('age_restr')
        fandoms = request.form.get('fandoms')
        file_name = str(Text.get_next_id()) + '.txt'
        f.open(file_name, 'w')
        for i in request.form.get('text'):
            f.write(i + '\n')
        f.close()
        new_text.text_file = file_name
        new_text.write_to_db(user)
        return render_template(upload_done.html)

    return render_template(
        'upload.html', 
        age_restrs=Text.get_age_restrs(),
        tags=Tag.get_all_tags(),
        fandoms=Fandom.get_all_fandoms()
    )


@main.route('/sign_up')
def sign_up():
    form = SignUpForm()
    return render_template('auth/signup.html', form=form)


@main.route('/login')
def login():
    return render_template('login.html')
