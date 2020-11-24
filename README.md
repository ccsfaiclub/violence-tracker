# violence-tracker
![Screenshot](violence-tracker-map.png)

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

Run the app:
```
make app_up
```

Stop PostgresSQL:
```
make docker_down
```