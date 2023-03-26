from . import main
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, current_user, logout_user
from ..models import User, Text, Tag, Fandom

import hashlib


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
        return render_template(
            'search_results.html',
            texts=Text.search_request(
                title=request.form.get('title'),
                tags=request.form.getlist('tags'),
                age_restr=request.form.get('age_restr')
            )
        )

    return render_template(
        'search.html',
        age_restrs=Text.get_age_restrs(),
        tags=Tag.get_all_tags(),
        fandoms=Fandom.get_all_fandoms()
    )


@main.route('/user/<username>')
def user(username):
    # TODO if logged in show link to profile in navbar
    user = User.get_user_by_username(username=username)
    texts = user.get_texts()
    return render_template('user.html', user=user, texts=texts)


@main.route('/upload')
@login_required
def upload():
    return render_template('upload.html')


@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST' and request.form.get('submit') == 'submit':
        username: str = request.form.get('username')
        email: str = request.form.get('email')
        password: str = hashlib.md5(request.form.get('password').encode('utf-8')).hexdigest()

        # check if all fields are not empty
        if username != '' and email != '' and password != '':
            username_is_available = User.username_is_available(username)
            email_is_available = User.email_is_available(email)
            if username_is_available and email_is_available:
                # write new user to db
                user = User(
                    id=None,
                    username=username,
                    email=email,
                    password=password,
                )
                user.write_to_db()
                # set user status as logged in
                login_user(user, remember=True)
            else:
                if not username_is_available:
                    flash('Такое имя пользователя уже занято.')
                if not email_is_available:
                    flash('Такая почта уже привязана к другому аккаунту.')

        return redirect(url_for('main.index', current_user=current_user))

    return render_template('signup.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and request.form.get('submit') == 'submit':
        email: str = request.form.get('email')
        password: str = hashlib.md5(request.form.get('password').encode('utf-8')).hexdigest()
        # check if there is a registered user with given email
        if not User.email_is_available(email):
            user = User.get_user_by_email(email)
            if user.password == password:
                # login here
                login_user(user, remember=True, force=True)
                print(current_user)
            else:
                flash('Пароль не подходит.')
                # TODO alert on incorrect password
                print('wrong password')
        else:
            print('nowhere')
            # TODO suggest to sign up

        return redirect(url_for('main.index', current_user=current_user))

    return render_template('login.html')


@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('main.index'))
