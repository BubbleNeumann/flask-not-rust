

## Project design

![design.jpg](https://raw.githubusercontent.com/BubbleNeumann/flask-not-rust/master/design.jpg)

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
├── venv/
└── setup.py
```

#### Run app

$ flask --app flask_not_rust run
