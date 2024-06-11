from flask import Blueprint

movies_bp = Blueprint('movies', __name__)
# reviews_bp = Blueprint('reviews', __name__)

from . import movies
