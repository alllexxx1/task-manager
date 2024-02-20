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

make-migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

make-messages:
	poetry run django-admin makemessages --ignore="static" --ignore=".env" -l ru

compile-messages:
	poetry run django-admin compilemessages

shell:
	poetry run python manage.py shell_plus

run-tests:
	poetry run python manage.py test

coverage:
	poetry run coverage run --source='.' manage.py test

coverage-report:
	poetry run coverage report

coverage-report-xml:
	poetry run coverage xml

coverage-report-html:
	poetry run coverage html

test-coverage:
	poetry run coverage run --source='.' manage.py test
	poetry run coverage xml

selfcheck:
	poetry check

check: selfcheck lint run-tests
