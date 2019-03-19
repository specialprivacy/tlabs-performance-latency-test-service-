FROM python:3

RUN apt-get update
WORKDIR /app

RUN pip install pyyaml
RUN pip install filepath
RUN pip install kafka-python
RUN pip install requests

COPY ./app/ /app/

CMD python app.py
