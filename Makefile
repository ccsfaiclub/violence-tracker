MAKEFILE_PATH = $(abspath $(lastword $(MAKEFILE_LIST)))
ROOT_FOLDER = $(shell dirname $(MAKEFILE_PATH))

docker_up:
	docker-compose run dependencies

docker_down:
	docker-compose down --volumes

docker_reset: docker_down docker_up

fe_install:
	cd frontend && npm install

fe_dev_up: fe_install
	cd frontend && npm start

create_and_populate_db:
	PYTHONPATH="$(ROOT_FOLDER)" python backend/create_and_populate_db.py

flask_up:
	PYTHONPATH="$(ROOT_FOLDER)" FLASK_APP=app.py cd backend && flask run

dump_db:
	pg_dump -h localhost -p 5432 -U postgres postgres

backend_tests:
	cd backend/tests && $(BACKEND_FLAGS) pytest --cov=backend --cov-report html:htmlcov
