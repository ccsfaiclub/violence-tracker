from backend.extensions import db

from backend.model import Incident, Location


def test_run_query(app, client):
    # Given: An incident exists in our DB
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
