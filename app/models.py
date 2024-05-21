from flask import current_app, g
import sqlite3

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', ''))
        g.db.row_factory = sqlite3.Row
    return g.db