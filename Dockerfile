FROM python:3.6.8-jessie

RUN apt-get update
WORKDIR /app

RUN pip install kafka-python

RUN mkdir -p /logs

COPY ./app/ /app/

CMD python app.py
