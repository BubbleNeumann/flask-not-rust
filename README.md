
**features to mention:**
* login required for upload (automatic redirect)
* alert on sign up if username or email is not available
* user session id shown in url is encrypted by md5 via User.\_\_repr__ overload
* alert on login if email wasn't found in db
* upload: limitations on title, description, and text min length

![index-screen.jpg](https://raw.githubusercontent.com/BubbleNeumann/flask-not-rust/master/docs/index-screen.jpg)

![login-screen.jpg](https://raw.githubusercontent.com/BubbleNeumann/flask-not-rust/master/docs/login-screen.jpg)

## Project design

![design.jpg](https://raw.githubusercontent.com/BubbleNeumann/flask-not-rust/master/docs/design.jpg)

### Project structure example

```
├── app/
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
