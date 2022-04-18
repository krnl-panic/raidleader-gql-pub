# Image official Python 3.9
FROM python:3.9-slim-bullseye as base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

FROM base AS raidleader-gql
RUN apt-get update && apt-get install -y --no-install-recommends gcc

RUN python -m pip install poetry

COPY pyproject.toml .
COPY poetry.lock .

RUN python -m poetry config virtualenvs.create false
RUN python -m poetry install --no-dev

RUN mkdir /app
WORKDIR /app

COPY . .

EXPOSE 8000

CMD [ "gunicorn","asgi:app","--preload","--workers","4","--bind","0.0.0.0:8000","--worker-class","uvicorn.workers.UvicornWorker"]
