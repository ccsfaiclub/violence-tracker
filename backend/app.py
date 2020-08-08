import graphene
from flask import Flask, app
from flask_cors import CORS

from backend import schema
from backend.extensions import db
from flask_graphql import GraphQLView

from backend.schema import schema


class BaseConfig(object):
    """Return config for Flask"""
    DB_HOST = 'localhost'
    DB_PORT = 5432
    DB_USERNAME = 'postgres'
    DB_PASSWORD = ''
    DB_NAME = 'postgres'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(BaseConfig())

    # initialize SqlAlchemy with flask config
    db.init_app(app)

    # this will add /graphql and /graphiql endpoints to app
    app.add_url_rule(
        "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
    )

    return app
