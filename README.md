# violence-tracker
![violence-tracker](https://user-images.githubusercontent.com/18561714/100044274-1db25b00-2dc4-11eb-9656-50ff0306854b.png)


### Prerequisites
You will need to have these programs installed in your environment:
 * [Docker](https://docs.docker.com/get-docker/)
 * [Docker-compose](https://docs.docker.com/compose/install/)
 * [Python 3.7+](https://www.python.org/downloads/)
 * [GNU Make](https://www.gnu.org/software/make/)

## Getting started 

Get the project code:
```
git clone https://github.com/ccsfaiclub/violence-tracker.git
cd violence-tracker/
```

Create a Python virtual environment:
```
virtualenv -p $(which python3) venv
source venv/bin/activate
```

Install the dependencies:
```
pip install -r backend/requirements.txt
```

Fire up PostgresSQL:
```
make docker_up
```

Build the database:
```
make create_and_populate_db
```

## Running the app:
```
make flask_up
make fe_dev_up
```

Stop PostgresSQL:
```
make docker_down
```
