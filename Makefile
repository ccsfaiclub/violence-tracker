docker_up:
	docker-compose run dependencies

docker_down:
	docker-compose down --volumes

fe_install:
	cd frontend && npm install

fe_dev_up: fe_install
	cd frontend && npm start

app_up:
	export PYTHONPATH=$(pwd)
	python backend/main.py

