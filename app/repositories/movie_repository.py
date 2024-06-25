from ..models import get_db

class MovieRepository:
    @staticmethod
    def get_all():
        db = get_db()
        with db.cursor() as cursor:
            cursor.execute('SELECT * FROM movies')
            movies = cursor.fetchall()
        return [dict(movie) for movie in movies] # python list comprehension
        #my_results = []
        #for movie in movies:
        #    my_results.append(dict(movie))
        #return my_results

    @staticmethod
    def get_by_id(movie_id):
        db = get_db()
        # parametrized sql statements protect us from SQL injection attacks
        with db.cursor as cursor:
            cursor.execute('SELECT * FROM movies WHERE id = %s', (movie_id, ))
            movie = cursor.fetchone()
        return dict(movie) if movie else None

    @staticmethod
    def add(data):
        db = get_db()
        with db.cursor() as cursor:
            cursor.execute('INSERT INTO movies (title) VALUES (%s)', (data['title'],))
            db.commit()
        return {'message':'movie added'}

    @staticmethod
    def update(movie_id, data):
        db = get_db()
        with db.cursor() as cursor:
            cursor.execute('UPDATE movies SET title = %s WHERE id = %s', (data['title'], movie_id))
            db.commit()
        return {'message':'movie updated'}

    @staticmethod
    def delete(movie_id):
        db = get_db()
        with db.cursor() as cursor:
            cursor.execute('DELETE FROM reviews WHERE movie_id = %s', (movie_id,))
            cursor.execute('DELETE FROM movies WHERE id = %s', (movie_id,))
            db.commit()
        return {'message':'movie deleted'}



