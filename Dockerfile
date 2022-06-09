FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
COPY app.py .
COPY celery_worker.py .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt


