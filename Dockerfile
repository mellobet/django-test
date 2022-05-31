FROM python:3.8.12-alpine3.14

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk add --update --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    python3-dev \
    libffi-dev

RUN pip install poetry==1.1.12

WORKDIR /app

COPY . .

RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi