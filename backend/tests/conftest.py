import pytest

from backend.app import create_app, BaseConfig
from backend.extensions import db


class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f'postgresql://postgres:@localhost:5432/postgres'


@pytest.fixture
def app():
    app = create_app(TestConfig())
    with app.app_context():
        db.drop_all()
        db.create_all()

    yield app


@pytest.fixture
def client(app):
    return app.test_client()

