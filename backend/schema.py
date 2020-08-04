from backend.extensions import db
from backend.model import Incident as IncidentModel

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType


class Incident(SQLAlchemyObjectType):
    class Meta:
        model = IncidentModel


class Query(graphene.ObjectType):
    incidents = graphene.List(Incident)

    def resolve_incidents(self, info):
        query = Incident.get_query(info)  # SQLAlchemy query
        return query.all()


