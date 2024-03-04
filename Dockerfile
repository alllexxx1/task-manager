FROM python:3.10 as base

SHELL ["/bin/bash", "-c"]

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWEITEBYTECODE 1

WORKDIR /app

COPY . .

RUN pip install "poetry==1.7.0"
RUN poetry config virtualenvs.create false
RUN poetry config installer.max-workers 1


FROM base as dev

RUN poetry install --no-interaction --no-ansi

CMD ["python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]


FROM base as prod

RUN poetry install --without dev --no-interaction --no-ansi
