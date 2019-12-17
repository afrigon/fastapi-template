FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

MAINTAINER Alexandre Frigon "fastapi-docker@frigon.app"

RUN rm -rf /app
WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./main.py ./
COPY ./app /app/app

