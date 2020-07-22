from flask import Flask

from backend.extensions import db

class BaseConfig(object):
    """Return config for Flask"""
    DB_HOST = 'localhost'
    DB_PORT = 5432
    DB_USERNAME= 'postgres'
    DB_PASSWORD= ''
    DB_NAME= 'postgres'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def create_app():
    app = Flask(__name__)

    app.config.from_object(BaseConfig())

    # initialize SqlAlchemy with flask config
    db.init_app(app)

    return app
