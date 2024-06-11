from flask import current_app, g
import sqlite3


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', ''))
        g.db.row_factory = sqlite3.Row
    return g.db

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

def close_db():
    db = g.pop('db', None)
    if db is not None:
        db.close()

def create_tables_if_not_exist():
    db = get_db()
    db.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        title TEXT NOT NULL 
    )
    """)
    db.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            movie_id INTEGER, 
            review TEXT,
            FOREIGN KEY (movie_id) REFERENCES movies (id)
        )
        """)

    db.commit()