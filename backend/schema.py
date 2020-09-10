from backend import app, model
from backend.extensions import db
from backend.model import Incident as IncidentModel
from backend.model import Location as LocationModel

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType


class Incident(SQLAlchemyObjectType):
    class Meta:
        model = IncidentModel


class Location(SQLAlchemyObjectType):
    class Meta:
        model = LocationModel


class Query(graphene.ObjectType):
    locations = graphene.List(Location)
    incidents = graphene.List(Incident)
    get_total_incidents = graphene.Int()
    get_total_distinct_states = graphene.Int()
    get_total_distinct_cities = graphene.Int()

    def resolve_get_total_incidents(self, info):
        return db.session.query(model.Incident).count()

    def resolve_get_total_distinct_states(self, info):
        return db.session.query(model.Location.state).distinct().count()

    def resolve_get_total_distinct_cities(self, info):
        return db.session.query(model.Location.city).distinct().count()

    def resolve_locations(self, info):
        query = Location.get_query(info)
        return query.all()

    def resolve_incidents(self, info):
        query = Incident.get_query(info)
        return query.filter(model.Incident.location_id != None).all()


schema = graphene.Schema(query=Query)
