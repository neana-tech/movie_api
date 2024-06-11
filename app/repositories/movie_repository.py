from ..models import get_db

class MovieRepository:
    @staticmethod
    def get_all():
        db = get_db()
        movies = db.execute('SELECT * FROM movies').fetchall()
        return [dict(movie) for movie in movies] # python list comprehension
        #my_results = []
        #for movie in movies:
        #    my_results.append(dict(movie))
        #return my_results

    @staticmethod
    def get_by_id(movie_id):
        db = get_db()
        # parametrized sql statements protect us from SQL injection attacks
        movie = db.execute('SELECT * FROM movies WHERE id = ?', (movie_id, )).fetchone()
        return dict(movie) if movie else None

    @staticmethod
    def add(data):
        db = get_db()
        db.execute('INSERT INTO movies (title) VALUES (?)', (data['title'],))
        db.commit()
        return {'message':'movie added'}

    @staticmethod
    def update(movie_id, data):
        db = get_db()
        db.execute('UPDATE movies SET title = ? WHERE id = ?', (data['title'], movie_id))
        db.commit()
        return {'message':'movie updated'}

    @staticmethod
    def delete(movie_id):
        db = get_db()
        db.execute('DELETE FROM movies WHERE id = ?', (movie_id,))
        db.commit()
        return {'message':'movie deleted'}



