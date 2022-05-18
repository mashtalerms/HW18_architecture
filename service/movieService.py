from dao.movieDao import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_all(self):
        return self.movie_dao.get_all()

    def get_one(self, mid):
        return self.movie_dao.get_one(mid)

    def get_by_director(self, director_id: int):
        return self.movie_dao.get_by_director(director_id)

    def get_by_genre(self, genre_id: int):
        return self.movie_dao.get_by_genre(genre_id)

    def get_by_year(self, year: int):
        return self.movie_dao.get_by_year(year)

    def create(self, data):
        return self.movie_dao.create(data)

    def update(self, data, mid):
        movie = self.movie_dao.get_one(mid)
        movie.title = data['title']
        movie.description = data['description']
        movie.trailer = data['trailer']
        movie.year = data['year']
        movie.rating = data['rating']
        movie.genre_id = data['genre_id']
        movie.director_id = data['director_id']

        return self.movie_dao.update(movie)

    def update_partial(self, data, mid):
        movie = self.movie_dao.get_one(mid)
        if 'title' in data:
            movie.title = data['title']
        if 'description' in data:
            movie.description = data['description']
        if 'trailer' in data:
            movie.trailer = data['trailer']
        if 'year' in data:
            movie.year = data['year']
        if 'rating' in data:
            movie.rating = data['rating']
        if 'genre_id' in data:
            movie.genre_id = data['genre_id']
        if 'director_id' in data:
            movie.director_id = data['director_id']

        return self.movie_dao.update(movie)

    def delete(self, mid: int):
        return self.movie_dao.delete(mid)
