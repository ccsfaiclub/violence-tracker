from sqlalchemy.dialects.postgresql import JSONB

from backend.extensions import db


class Incident(db.Model):
    __tablename__ = 'incidents'

    id = db.Column(db.Integer, primary_key=True)
    links = db.Column(JSONB)
    state = db.Column(db.String)
    city = db.Column(db.String)
    description = db.Column(db.String)
    tags = db.Column(JSONB)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.String)
    date_text = db.Column(db.String)
