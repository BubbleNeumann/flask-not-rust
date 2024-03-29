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


@main.route('/user/<username>', methods=['GET', 'POST'])
def user(username):
    user = User.get_user_by_username(username=username)
    if request.method == 'POST':
        if request.form.get('ban') == 'ban':
            user.update_role(new_role_id=3)
        if request.form.get('ban') == 'no-ban':
            user.update_role(new_role_id=2)
        if not request.form.get('remove') is None:
            text_id = request.form.get('remove')
            Text.get_text_by_id(text_id).delete_from_db()

    texts = user.get_texts()
    return render_template(
        'user.html',
        user=user,
        texts=texts,
        texts_cnt=len(texts)
    )


@main.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST' and request.form.get('submit') == 'upload':
        title = request.form.get('title')
        desc = request.form.get('descr')
        text = request.form.get('text')

        tags = request.form.getlist('tags')
        fandoms = request.form.getlist('fandoms')

        age_restr = request.form.get('age_restr')

        if len(text) < 100:
            flash('Текст не может быть короче 100 символов.')
        elif len(desc) < 100:
            flash('Описание не может быть короче 100 символов.')
        elif len(title) < 3:
            flash('Название работы не может быть короче 3 символов.')
        elif len(tags) == 0:
            flash('Укажите хотя бы один тег.')
        elif len(fandoms) == 0:
            flash('Укажите хотя бы один фандом.')
        elif age_restr is None:
            flash('Укажите возрастное ограничение.')
        else:
            from datetime import date
            int_restr = 0
            match age_restr:
                case 'G':
                    int_restr = 6
                case 'PG-13':
                    int_restr = 13
                case 'R':
                    int_restr = 17
                case 'NC':
                    int_restr = 21
            new_text = Text(
                id=None,
                title=title,
                text_file=text,
                release_date=date.today(),
                lang=None,
                descr=desc,
                age_restr=int_restr
            )
            new_text.write_to_db(
                user_id=current_user.id,
                tags=tags,
                fandoms=fandoms
            )
            return redirect(url_for('main.user', username=current_user.username))

    return render_template(
        'upload.html',
        tags=Tag.get_all_tags(),
        fandoms=Fandom.get_all_fandoms(),
        age_restrs=Text.get_age_restrs()
    )


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
        user = User.get_user_by_email(email)
        if not User.email_is_available(email) and user.password == password:
            login_user(user, remember=True, force=True)
        else:
            flash('Некорректно введены почта или пароль.')
            return render_template('login.html')

        return redirect(url_for('main.index', current_user=current_user))

    return render_template('login.html')


@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('main.index'))
