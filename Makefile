install:
	poetry install

build:
	./build.sh

dev:
	poetry run python manage.py runserver

PORT ?= 8000
start:
	poetry run gunicorn -w 4 -b 0.0.0.0:$(PORT) task_manager.wsgi:application

lint:
	poetry run flake8

collect-static:
	poetry run python manage.py collectstatic --no-input

migrate:
	poetry run python manage.py migrate
