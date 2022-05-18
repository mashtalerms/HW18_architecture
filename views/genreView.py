from flask_restx import Resource, Namespace
from container import genre_service
from dao.model.genreModel import GenreSchema

genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        return genres_schema.dump(genre_service.get_all()), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        return genre_schema.dump(genre_service.get_one(gid)), 200
