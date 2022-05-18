from flask import request
from flask_restx import Resource, Namespace
from dao.model.movieModel import MovieSchema
from container import movie_service

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")
        year = request.args.get("year")
        if director_id:
            return movies_schema.dump(movie_service.get_by_director(director_id)), 200
        elif genre_id:
            return movies_schema.dump(movie_service.get_by_genre(genre_id)), 200
        elif year:
            return movies_schema.dump(movie_service.get_by_year(year)), 200
        else:
            return movies_schema.dump(movie_service.get_all()), 200

    def post(self):
        data = request.get_json()
        movie_service.create(data)
        return '', 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        return movie_schema.dump(movie_service.get_one(mid)), 200

    def put(self, mid):
        data = request.get_json()
        movie_service.update(data, mid)
        return '', 201

    def patch(self, mid):
        data = request.get_json()
        movie_service.update_partial(data, mid)
        return '', 201

    def delete(self, mid):
        return movie_service.delete(mid), 204
