FROM python:3.11-alpine3.18

COPY requirements.txt /tmp/requirements.txt

RUN apk add postgresql-client build-base postgresql-dev
RUN pip install -r /tmp/requirements.txt
RUN adduser --disabled-password scheduler-user
USER scheduler-user

COPY scheduler /scheduler
WORKDIR /scheduler
EXPOSE 8000
