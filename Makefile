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

fe_build_prod: fe_install
	cd frontend && PUBLIC_URL='https://hoeunsim.com/vt' npm run-script build

fe_prod_deploy: fe_build_prod
	cd frontend && scp -r build root@hoeunsim.com:/var/www/html/vt

create_and_populate_db:
	PYTHONPATH="$(ROOT_FOLDER)" python backend/create_and_populate_db.py

flask_up:
	PYTHONPATH="$(ROOT_FOLDER)" FLASK_APP=app.py cd backend && flask run --port 5001

flask_prod_up:
	PYTHONPATH="$(ROOT_FOLDER)" FLASK_APP=app.py cd backend && flask run --host=0.0.0.0 --port 5001

dump_db:
	pg_dump -h localhost -p 5432 -U postgres postgres

backend_tests:
	cd backend/tests && $(BACKEND_FLAGS) pytest --cov=backend --cov-report html:htmlcov
