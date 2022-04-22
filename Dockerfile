# Image official Python 3.9
FROM python:3.9-slim-bullseye

ARG DB_DSN=""
ENV DB_DSN $DB_DSN

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

RUN apt-get update && apt-get install -y --no-install-recommends gcc

RUN python -m pip install poetry

COPY pyproject.toml .
COPY poetry.lock .

RUN python -m poetry config virtualenvs.create false
RUN python -m poetry install --no-dev

RUN mkdir /app
WORKDIR /app

COPY . .

CMD exec gunicorn asgi:app --preload --workers 1 --threads 8 --bind :$PORT --timeout 0 --worker-class "uvicorn.workers.UvicornWorker"
