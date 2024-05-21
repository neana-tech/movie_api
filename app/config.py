import os


class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', f'sqlite:///{os.path.join(basedir, "movies.db")}')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


database_path = os.path.join(Config.basedir, "movies.db")
if not os.path.exists(os.path.dirname(database_path)):
    os.makedirs(os.path.dirname(database_path), exist_ok=True)
