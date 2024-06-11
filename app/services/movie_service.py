from ..repositories.movie_repository import MovieRepository

class MovieService:
    @staticmethod
    def get_movies():
        return MovieRepository.get_all()


    @staticmethod
    def get_movie(movie_id):
        return MovieRepository.get_by_id(movie_id)

    @staticmethod
    def add_movie(data):
        return MovieRepository.add(data)

    @staticmethod
    def update_movie(movie_id,data):
        return MovieRepository.update(movie_id,data)

    @staticmethod
    def delete_movie(movie_id):
        return MovieRepository.delete(movie_id)

