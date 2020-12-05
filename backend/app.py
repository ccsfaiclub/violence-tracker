import graphene
from flask import Flask
from flask_cors import CORS

from backend import schema
from backend.config import BaseConfig
from backend.extensions import db
from flask_graphql import GraphQLView

from backend.schema import schema


def create_app(config=BaseConfig()):
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(config)

    # initialize SqlAlchemy with flask config
    db.init_app(app)

    # this will add /graphql and /graphiql endpoints to app
    app.add_url_rule(
        "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
    )

    return app

