from celery import Celery
import celery
import os

celery = Celery(__name__)

celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "localhost")
celery.conf.result_backend = os.environ.get(
    "CELERY_RESULT_BACKEND", "localhost")


@celery.task(name="create_task")
def create_task(a, b, c):
    print(a)
    return b + c
