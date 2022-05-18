from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.directorView import director_ns
from views.genreView import genre_ns
from views.movieView import movie_ns


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()
    configure_app(app)
    return app


def configure_app(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    # load_data(app, db)


# def load_data(app, db):
#     with app.app_context():
#         db.create_all()


app_config = Config()
app = create_app(app_config)


if __name__=='__main__':
    app.run(debug=True)