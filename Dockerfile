FROM python:3-alpine

RUN apk add build-base

ADD . /app
WORKDIR /app

RUN pip install gunicorn
RUN pip install -r requirements.txt
