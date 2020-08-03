from backend.extensions import db
from backend.model import Incident as IncidentModel

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType


class Incident(SQLAlchemyObjectType):
    class Meta:
        model = IncidentModel
        # interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    # node = relay.Node.Field()
    # # Allow only single column sorting
    # all_incidents = SQLAlchemyConnectionField(
    #     Incident.connection, sort=Incident.sort_argument())
    # # Allows sorting over multiple columns, by default over the primary key
    # all_incidents = SQLAlchemyConnectionField(Incident.connection)
    # # Disable sorting over this field
    # all_incidents = SQLAlchemyConnectionField(Incident.connection, sort=None)

    incidents = graphene.List(Incident)

    def resolve_incidents(self, info):
        query = Incident.get_query(info)  # SQLAlchemy query
        return query.all()


