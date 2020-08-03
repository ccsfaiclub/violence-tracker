import json

import graphene
from flask_graphql import GraphQLView

from backend import schema
from backend.schema import Incident, Query
from backend.app import create_app
from backend.extensions import db
from backend.model import Incident
from typing import List, Dict


def main():
    app = create_app()

    with app.app_context():
        db.create_all()

        write_to_db()

        run_query(query)


def get_data(json_file: str) -> List[Dict]:
    """
    Reads JSON file, parses the incidents data,
    and returns the data as a list of dictionaries
    """
    with open(json_file, 'r') as data_file:
        data = json.loads('\n'.join(data_file.readlines()))
        return data['data']


def write_to_db():
    """
    Gets the data, and using a loop, populates the db with
    each incident added as a row in the Incidents table

    Note: For now, loop only adds 3 incidents; we can change this to include all incidents later
    """
    data = get_data('../police-brutality-data.json')
    for i in range(3):
        links = data[i]['links']
        state = data[i]['state']
        city = data[i]['city']
        description = data[i]['description']
        tags = data[i]['tags']
        name = data[i]['name']
        date = data[i]['date']
        date_text = data[i]['date_text']

        incident = Incident(links=links,
                            state=state,
                            city=city,
                            description=description,
                            tags=tags,
                            name=name,
                            date=date,
                            date_text=date_text)

        db.session.add(incident)
    db.session.commit()


query = '''
        query {
            incidents {
                id,
                links,
                state,
                city,
                description,
                tags,
                name,
                date,
                dateText
            }
        }
        '''


def run_query(query: str):
    """
    Runs a query against schema and prints the results
    """
    schema = graphene.Schema(query=Query)
    result = schema.execute(query, context_value={'session': db})
    print(result)
    '''
    SAMPLE OUTPUT 
    {
       "data":{
          "incidents":[
             {
                "id":"1",
                "links":"[{\"url\": \"https://journalstar.com/news/local/crime-and-courts/watch-now-arrested-lincoln-protester-felt-violated-we-did-nothing-wrong-but-exercise-our-constitutional/article_aa0216d0-b79b-524b-9b6a-5db44a2d49dc.html\", \"text\": \"\"}, {\"url\": \"https://twitter.com/greg_doucette/status/1268772480153460736\", \"text\": \"\"}]",
                "state":"Nebraska",
                "city":"Lincoln",
                "description":"A crowd gathers around a woman who is being arrested. After she is pulled away, police give a dispersal order. Protestors comply, but appear to exchange words with officers while walking away. Police then shout that they are under arrest, shoving protestors to the ground and kneeling on them to make arrests.",
                "tags":"[\"arrest\", \"shove\", \"knee\", \"protestor\"]",
                "name":"Police arrest protestors leaving scene",
                "date":"2020-05-31",
                "dateText":"May 31st"
             },
             {
                "id":"2",
                "links":"[{\"url\": \"https://twitter.com/ChrisDunkerLJS/status/1268938853945167873\", \"text\": \"\"}, {\"url\": \"https://twitter.com/ChrisDunkerLJS/status/1268981851164684290\", \"text\": \"\"}]",
                "state":"Nebraska",
                "city":"Lincoln",
                "description":"A reporter posted a picture of a tear gas canister, allegedly used in Lincoln protests. In the tweet, he states he and his photographer were tear gassed twice by police.",
                "tags":"[\"journalist\", \"tear-gas\", \"tear-gas-canister\"]",
                "name":"Reporter shows tear gas canister fired at him by police",
                "date":"2020-05-31",
                "dateText":"May 31st"
             },
             {
                "id":"3",
                "links":"[{\"url\": \"https://twitter.com/XruthxNthr/status/1266903223220097024\", \"text\": \"\"}]",
                "state":"Nebraska",
                "city":"Omaha",
                "description":"A bunch of protesters peacefully sitting on the ground were shot at and maced. A group of police officers pushed these civilians on to the ground and hit them.",
                "tags":"[\"mace\", \"spray\", \"pepper-balls\", \"protestor\"]",
                "name":"Police Mace, shoot pepper bullets at protesters sitting on the ground",
                "date":"2020-05-31",
                "dateText":"May 31st"
             }
          ]
       }
    }
    '''


if __name__ == "__main__":
    main()
