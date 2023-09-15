FROM python:3.11-slim-buster
LABEL maintainer="starcrafter4444@gmail.com"

ENV PYTHONUMBUFFERED 1
WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

USER django-user