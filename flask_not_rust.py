from app import create_app
from flask_login import LoginManager
import keys
from app.models import User

app = create_app()
app.config['SECRET_KEY'] = keys.SECRET_KEY

login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id: int):
    return User.get_user_by_id(user_id)
