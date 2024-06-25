from flask import request,jsonify
from . import movies_bp
from ..services.movie_service import MovieService

@movies_bp.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(MovieService.get_movies())

@movies_bp.route('/movies/<int:id>', methods=['GET'])
def get_movie(id):
    return jsonify(MovieService.get_movie(id))

@movies_bp.route('/movies', methods=['POST'])
def add_movie():
    # data = {'title': 'Spiderman' }
    data = request.json
    return jsonify(MovieService.add_movie(data))

@movies_bp.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    data = request.json
    return jsonify(MovieService.update_movie(id, data))

@movies_bp.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    return jsonify(MovieService.delete_movie(id))

@movies_bp.route('/movies', methods=['DELETE'])
def delete_movies():
    return jsonify(MovieService.delete_movies())