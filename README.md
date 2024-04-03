### Hexlet tests and linter status:
[![Actions Status](https://github.com/alllexxx1/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/alllexxx1/python-project-52/actions)
[![Actions Status](https://github.com/alllexxx1/python-project-52/actions/workflows/task-manager.yml/badge.svg)](https://github.com/alllexxx1/python-project-52/actions)
\
[![Maintainability](https://api.codeclimate.com/v1/badges/20a17e8d69796724e897/maintainability)](https://codeclimate.com/github/alllexxx1/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/20a17e8d69796724e897/test_coverage)](https://codeclimate.com/github/alllexxx1/python-project-52/test_coverage)

---

# [Task manager](https://task-manager-kli2.onrender.com/)


![Task manager](https://imgur.com/kxRHfN0.png)
![Task manager](https://imgur.com/iN5h3e6.png)


#### Run the project both locally and on a production server
```
$ git clone git@github.com:alllexxx1/python-project-52.git
$ cd python-project-52
$ make install

# at this point create a '.env' file and set up
# configuration variables (example below)

$ make migrate
$ make dev # start the app locally
$ make start # command to launch the app on a production server

# for more useful shortcut commands check out the Makefile
```
#### .env file example
```
SECRET_KEY=any_reliable_set_of_characters
DATABASE_URL=postgres://youruser:yourpassword@localhost:5432/yourdatabase
DEBUG=True # /False
ROLLBAR_ACCESS_TOKEN=token_provided_by_roolbar.com
```
#### Useful commands for development 
```
$ make run-test
$ make coverage
$ make shell
```

---

### Links

This project was built using these tools:

| Tool                                                                             | Description                                                                                                                                     |
|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [django](https://docs.djangoproject.com/en/5.0/)                                 | "High-level Python web framework that encourages rapid development and clean, pragmatic design"                                                 |
| [gunicorn](https://docs.gunicorn.org/en/stable/)                                 | " ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX"                                                                                        |
| [poetry](https://python-poetry.org/)                                             | "Python dependency management and packaging made easy"                                                                                          |
| [flake8](https://flake8.pycqa.org/)                                              | "Your tool for style guide enforcement"                                                                                                         |
| [django-bootstrap](https://django-bootstrap5.readthedocs.io/en/stable/)          | "Django-bootstrap provides template tags and tools for easily incorporating Bootstrap's styles and components into Django templates"            |
| [django-bootstrap-icons](https://github.com/christianwgd/django-bootstrap-icons) | "A quick way to add Bootstrap Icons with Django template tags"                                                                                  |
| [django-filters](https://github.com/theskumar/python-dotenv)                     | "Generic, reusable application to alleviate writing some of the more mundane bits of view code"                                                 |
| [dj-database-url](https://github.com/jazzband/dj-database-url)                   | "This simple Django utility allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application" |
| [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)                     | "PostgreSQL database adapter for the Python programming language"                                                                               |
| [python-dotenv](https://github.com/theskumar/python-dotenv)                      | "A library that helps load configuration from a .env"                                                                                           |