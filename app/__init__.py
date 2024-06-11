from flask import Flask
from .config import Config
from .models import create_tables_if_not_exist
from .routes import movies_bp

def create_app():
    app = Flask(__name__)
    print("this : : " + __name__)
    app.config.from_object(Config)

    with app.app_context():
        create_tables_if_not_exist()

    app.register_blueprint(movies_bp)

    return app
