from backend.extensions import db

from backend.model import Incident, Location


def add_incident(app):
    """
    Helper function to load an incident into the DB
    """
    with app.app_context():
        incident1 = Incident(external_id='1',
                             links=[],
                             tags=[],
                             date="2020-05-29",
                             date_text="May 29th",
                             name="Police arrest a man for speaking at them from a distance",
                             description="Officer line moves protesters back and as protesters comply they attempt to arrest a man that was not visibly violent.",
                             city="Las Vegas",
                             state="Nevada",
                             location=Location(city='Las Vegas', state='Nevada'))
    db.session.add(incident1)
    db.session.commit()


def test_get_incidents(app, client):
    # Given: An incident exists in our DB
    with app.app_context():
        add_incident(app)

        # When: We query for an incident
        query = """
                 {
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
                """

        incidents_count = db.session.query(Incident).count()

    # Then: We should get back 1 result
    assert incidents_count == 1

    rv = client.get('/graphql', json={'query': query})
    # Then: The result should contain information about that incident
    assert rv.get_json() == {'data': {'incidents': [{'city': 'Las Vegas',
                                                     'date': '2020-05-29',
                                                     'dateText': 'May 29th',
                                                     'description': 'Officer line moves protesters back '
                                                                    'and as protesters comply they attempt '
                                                                    'to arrest a man that was not visibly '
                                                                    'violent.',
                                                     'id': '1',
                                                     'links': '[]',
                                                     'name': 'Police arrest a man for speaking at them '
                                                             'from a distance',
                                                     'state': 'Nevada',
                                                     'tags': '[]'}]}}


def test_get_locations(app, client):
    # Given: An incident (with a location) exists in our DB
    with app.app_context():
        add_incident(app)

        # When: We query for locations
        query = """
                {
                locations {
                    id,
                    city,
                    state,
                    lon,
                    lat
                    }
                }
                """

        locations_count = db.session.query(Incident).count()

    # Then: We should get back 1 result
    assert locations_count == 1

    rv = client.get('/graphql', json={'query': query})
    # Then: The result should contain information about that location
    assert rv.get_json() == {
        "data": {
            "locations": [
                {
                    "id": "1",
                    "city": "Las Vegas",
                    "state": "Nevada",
                    "lon": None,
                    "lat": None
                }
            ]
        }
    }


def test_get_total_incidents(app, client):
    # Given: Two incidents exists in our DB
    with app.app_context():
        add_incident(app)
        add_incident(app)

        # When: We query for total incidents
        query = """
                {
                    getTotalIncidents
                }
                """

        incidents_count = db.session.query(Incident).count()

    # Then: We should get back 2 results
    assert incidents_count == 2

    rv = client.get('/graphql', json={'query': query})

    # Then: The result should contain 2 as the value for 'getTotalIncidents'
    assert rv.get_json() == {
        "data": {
            "getTotalIncidents": 2
        }
    }


def test_get_distinct_states(app, client):
    # Given: Two incidents from different states
    with app.app_context():
        add_incident(app)
        incident2 = Incident(external_id='2',
                             links=[],
                             tags=[],
                             date="2020-05-29",
                             date_text="May 29th",
                             name="Police arrest a man for speaking at them from a distance",
                             description="Officer line moves protesters back and as protesters comply they attempt to arrest a man that was not visibly violent.",
                             city="San Francisco",
                             state="California",
                             location=Location(city='San Francisco', state='California'))
        db.session.add(incident2)
        db.session.commit()

        # When: We query for total distinct states
        query = """
                {
                    getTotalDistinctStates
                }
                """

        incidents_count = db.session.query(Incident).count()

    # Then: We should get back 2 for our incidents count
    assert incidents_count == 2

    rv = client.get('/graphql', json={'query': query})

    # Then: The result should indicate that we have a total of 2 distinct states
    assert rv.get_json() == {
        "data": {
            "getTotalDistinctStates": 2
        }}


def test_get_distinct_cities(app, client):
    # Given: Two incidents from different cities (but the same state) exist in our DB
    with app.app_context():
        add_incident(app)
        incident2 = Incident(external_id='2',
                             links=[],
                             tags=[],
                             date="2020-05-29",
                             date_text="May 29th",
                             name="Police arrest a man for speaking at them from a distance",
                             description="Officer line moves protesters back and as protesters comply they attempt to arrest a man that was not visibly violent.",
                             city="Reno",
                             state="Nevada",
                             location=Location(city='Reno', state='Nevada'))
        db.session.add(incident2)
        db.session.commit()

        # When: We query for total distinct cities
        query = """
                {
                    getTotalDistinctCities
                }
                """

        incidents_count = db.session.query(Incident).count()

    # Then: We should get back 2 for our incidents count
    assert incidents_count == 2

    rv = client.get('/graphql', json={'query': query})

    # Then: The result should indicate that we have a total of 2 distinct cities
    assert rv.get_json() == {
        "data": {
            "getTotalDistinctCities": 2
        }}
