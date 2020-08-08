from flask_graphql import GraphQLView

from backend import app, model
from backend.extensions import db
from backend.model import Incident as IncidentModel
from backend.model import Location as LocationModel

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType


class Incident(SQLAlchemyObjectType):
    class Meta:
        model = IncidentModel


"""
class Query(graphene.ObjectType):
    incidents = graphene.List(Incident)

    def resolve_incidents(self, info):
        query = Incident.get_query(info)  # SQLAlchemy query
        return query.all()
"""


class Location(SQLAlchemyObjectType):
    class Meta:
        model = LocationModel


class Query(graphene.ObjectType):
    locations = graphene.List(Location)
    incidents = graphene.List(Incident)

    def resolve_locations(self, info):
        query = Location.get_query(info)  # SQLAlchemy query
        return query.all()

    def resolve_incidents(self, info):
        query = Incident.get_query(info)  # SQLAlchemy query
        return query.filter(model.Incident.location_id != None).all()


schema = graphene.Schema(query=Query)
