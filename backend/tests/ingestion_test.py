import json

from backend.create_and_populate_db import write_to_db, geocode_cities
from backend.extensions import db

from backend.model import Incident, Location


def test_load_data_into_db(app):
    # Given: A JSON object
    json_object = """
    {
      "edit_at": "https://github.com/2020PB/police-brutality",
      "help": "ask @ubershmekel on twitter",
      "updated_at": "2020-11-30T16:10:31.081504+00:00",
      "data": [
        {
          "links": [
            {
              "url": "https://twitter.com/itsraiialex/status/1266770032719040513",
              "text": ""
            }
          ],
          "state": "Nevada",
          "edit_at": "https://github.com/2020PB/police-brutality/blob/main/reports/Nevada.md",
          "city": "Las Vegas",
          "description": "Officer line moves protesters back and as protesters comply they attempt to arrest a man that was not visibly violent.",
          "tags": [
            "arrest",
            "protester"
          ],
          "geolocation": "36.1146208, -115.171627",
          "name": "Police arrest a man for speaking at them from a distance",
          "date": "2020-05-29",
          "date_text": "May 29th",
          "id": "nv-lasvegas-3"
        }
      ]
    }
    """
    # When: When load this object into our Postgres database
    with app.app_context():
        write_to_db(json.loads(json_object)['data'])
        geocode_cities()
        db.session.commit()

        # Then: The object will be inserted as a new incident row
        rows = db.session.query(Incident).count()
        assert rows == 1

        # Then: The Locations table will contain a new row for the incident's location
        rows = db.session.query(Location).count()
        assert rows == 1



