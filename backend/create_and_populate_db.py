import json

import graphene
from sqlalchemy import and_

from backend.app import create_app
from backend.extensions import db
from typing import List, Dict, Optional
import requests

from backend.model import Incident, Location
from backend.schema import Query


def main():
    app = create_app()

    with app.app_context():
        db.create_all()

        read_from_file_and_write_to_db()

        geocode_cities()

        # run_query(query)


def download_write_file() -> str:
    """
    Given a URL, retrieves and writes contents to json file.
    """
    url = 'https://raw.githubusercontent.com/2020PB/police-brutality/data_build/all-locations-v2.json'
    r = requests.get(url)

    json_object = json.dumps(r.json())

    data_file = 'police-brutality-data-all-locations.json'

    with open(data_file, 'w') as outfile:
        outfile.write(json_object)
    return data_file


def get_data(json_file: str) -> List[Dict]:
    """
    Reads JSON file, parses the incidents data,
    and returns the data as a list of dictionaries
    """
    with open(json_file, 'r') as data_file:
        data = json.loads('\n'.join(data_file.readlines()))
        return data['data']


def read_from_file_and_write_to_db():
    """
    Downloads the JSON file, parses the data, and writes it to the DB
    """
    file = download_write_file()
    data = get_data(file)

    return write_to_db(data)


def write_to_db(data: List[Dict]):
    """
    Loops through incidents data and populates the db with
    each incident added as a row in the Incidents table
    """
    for i in range(len(data)):
        id = data[i]['id']
        links = data[i]['links']
        state = data[i]['state']
        city = data[i]['city']
        description = data[i]['description']
        tags = data[i]['tags']
        name = data[i]['name']
        date = data[i]['date']
        date_text = data[i]['date_text']

        incident = Incident(external_id=id,
                            links=links,
                            state=state,
                            city=city,
                            description=description,
                            tags=tags,
                            name=name,
                            date=date,
                            date_text=date_text)

        db.session.add(incident)
    db.session.commit()


def get_location(city: str, state: str) -> Optional[Location]:
    """
    Looks up a location in the db by city and state.
    If the location exists, then we already have the lat, long.
    Otherwise, make a request to fetch the lat, long.
    """
    # Look up location if it exists already
    location = db.session.query(Location).filter(and_(
        Location.city == city,
        Location.state == state
    )).one_or_none()
    if location:
        return location

    # TODO write this as an internal endpoint rather than use requests to make the call
    query = f'https://nominatim.openstreetmap.org/search?city={city}&state={state}&format=json'
    response = requests.get(query)
    if response.status_code == 200:
        data = json.loads(response.text)
        if data:
            lat = data[0]['lat']
            lon = data[0]['lon']
            location = Location(city=city, state=state, lat=lat, lon=lon)
            db.session.add(location)
            return location
    return None


def geocode_cities():
    """
    Fetches all incidences loaded into the postgres db.
    Loops through all incidences and geocodes each location to get a lat, long.
    Populates the locations table with lat longs
    :return: None
    """
    # Loop through every incident using cursor (instead of loading all into memory)
    for incident in db.session.query(Incident):
        # incident_id = incident.id
        city = incident.city.lower().replace(' ', '+')
        state = incident.state.lower().replace(' ', '+')

        if city and state:
            incident.location = get_location(city, state)
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
                dateText,
                locationId
            }
        }
        '''


def run_query(query: str):
    """
    Runs a query against schema and returns the results
    """
    schema = graphene.Schema(query=Query)
    result = schema.execute(query, context_value={'session': db})

    return result


if __name__ == "__main__":
    main()
