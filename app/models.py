from flask import current_app, g
import psycopg2
from psycopg2.extras import DictCursor


def get_db():
    if 'db' not in g:
        uri = current_app.config['SQLALCHEMY_DATABASE_URI']
        g.db = psycopg2.connect(uri)
        g.db.cursor_factory = psycopg2.extras.DictCursor
    return g.db


def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        with db.cursor() as cursor:
            cursor.execute(f.read().decode('utf8'))
        db.commit()

def close_db():
    db = g.pop('db', None)
    if db is not None:
        db.close()

def create_tables_if_not_exist():
    db = get_db()
    with db.cursor() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id SERIAL PRIMARY KEY, 
            title TEXT NOT NULL 
        )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reviews (
                id SERIAL PRIMARY KEY, 
                movie_id INTEGER, 
                review TEXT,
                FOREIGN KEY (movie_id) REFERENCES movies (id)
            )
            """)
        db.commit()

