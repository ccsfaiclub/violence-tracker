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
<<<<<<< HEAD
	PYTHONPATH="$(ROOT_FOLDER)" python backend/create_and_populate_db.py
=======
  PYTHONPATH="$(ROOT_FOLDER)" python backend/create_and_populate_db.py
>>>>>>> 1bc8c1f778078926cb4218f01691881a923a056b

flask_up:
	PYTHONPATH="$(ROOT_FOLDER)" FLASK_APP=app.py cd backend && flask run

dump_db:
	pg_dump -h localhost -p 5432 -U postgres postgres

