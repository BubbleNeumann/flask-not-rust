## Project design

![design.jpg](https://github.com/BubbleNeumann/flask-not-rust/blob/master/design.jpg)

### Project sructure example

```
/home/user/Projects/flask
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
└── setup.py
```

### "How to" section
#### Run app

$ flask --app main run

#### Create the table

$ flask shell
from main import db
db.create_all()

#### Insert Rows

from main import User
user_a = User(username='a', email='a@email.com')
db.session.add(user_a)

alternatively:
db.session.add_all([user_a, user_b])

print(user_a.id)
db.session.commit()

#### Delete Rows

db.session.delete(user_a)
db.session.commit()


## TODO

- [x] sign up html template
- [ ] refactoring (in progress)
- [ ] if email is known -> suggest to login
- [ ] email verification (email sending)
- [ ] search page (/search)
- [ ] upload page (/upload)
- [ ] browse page (list of all texts): create blocks for db elems
- [ ] reading mode 
- [ ] if logged in redirect from auth pages
- [ ] ? upvotes
- [ ] ? cookies
