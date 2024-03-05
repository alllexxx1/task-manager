FROM python:3.10-slim as base

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWEITEBYTECODE 1

WORKDIR /app

COPY . .

RUN pip install "poetry==1.7.0"
RUN poetry config virtualenvs.create false
RUN poetry config installer.max-workers 1


FROM base as dev

RUN poetry install --no-interaction --no-ansi


FROM base as prod

RUN poetry install --without dev --no-interaction --no-ansi
