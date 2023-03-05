from app import create_app
import keys

app = create_app()
app.config['SECRET_KEY'] = keys.SECRET_KEY
