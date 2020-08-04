

docker_up:
	docker-compose run dependencies

docker_down:
	docker-compose down --volumes

app_up:
	export PYTHONPATH=$(pwd)
	python backend/main.py

