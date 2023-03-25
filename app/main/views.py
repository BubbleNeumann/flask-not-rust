from . import main
from flask import render_template, request
from ..models import User, Text, Tag, Fandom


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
    user = User.get_user_by_username(username=username)
    texts = user.get_texts()
    return render_template('user.html', user=user, texts=texts)


@main.route('/upload')
def upload():
    return render_template('upload.html')


@main.route('/sign_up')
def sign_up():
    pass


@main.route('/login')
def login():
    return render_template('login.html')
