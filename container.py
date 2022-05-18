from dao.directorDao import DirectorDAO
from dao.genreDao import GenreDAO
from service.directorService import DirectorService
from service.genreService import GenreService
from setup_db import db
from dao.movieDao import MovieDAO
from service.movieService import MovieService

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)
