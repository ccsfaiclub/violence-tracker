from sqlalchemy.dialects.postgresql import JSONB

from backend.config import BaseConfig
from backend.extensions import db


class Incident(db.Model):
    __tablename__ = 'incidents'

    # Prefer JSONB if we are using Postgres b/c it's a faster, binary, prettier format
    _JSON_COLUMN_TYPE = JSONB if 'postgresql' in BaseConfig.SQLALCHEMY_DATABASE_URI else db.JSON

    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.String)
    links = db.Column(_JSON_COLUMN_TYPE)
    state = db.Column(db.String)
    city = db.Column(db.String)
    description = db.Column(db.String)
    tags = db.Column(_JSON_COLUMN_TYPE)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.String)
    date_text = db.Column(db.String)

    # many-to-one relationship, as many incidents can occur in a single location
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), index=True)
    location = db.relationship('Location')


class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)

    city = db.Column(db.String)
    state = db.Column(db.String)

    lat = db.Column(db.Float)
    lon = db.Column(db.Float)


