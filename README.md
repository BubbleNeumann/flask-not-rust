
**features to mention:**
* login required for upload (automatic redirect)
* alert on sign up if username or email is not available
* user session id shown in url is encrypted by md5 via User.\_\_repr__ overload
* 

## Project design

![design.jpg](https://raw.githubusercontent.com/BubbleNeumann/flask-not-rust/master/design.jpg)

### Project structure example

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
├── venv/
└── setup.py
```

#### Run app

$ flask --app flask_not_rust run
