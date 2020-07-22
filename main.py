import json

from backend.app import create_app
from backend.extensions import db
from backend.model import Incident
from typing import List, Dict


def main():
    app = create_app()

    with app.app_context():
        db.create_all()

    write_to_db(app)

def get_data(json_file: str) -> List[Dict]:
    with open(json_file, 'r') as data_file:
        data = json.loads('\n'.join(data_file.readlines()))
        return data['data']

def write_to_db(app):
    with app.app_context():
        data = get_data('../police-brutality-data.json')
        for i in range(10):
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


if __name__ == "__main__":
    main()
