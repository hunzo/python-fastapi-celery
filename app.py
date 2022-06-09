from fastapi import FastAPI
from pydantic import BaseModel
from celery_worker import create_task
from datetime import datetime, timedelta

app = FastAPI()


class Payload(BaseModel):
    countdown_second: int
    x: int
    y: int


@app.post("/")
def index(data: Payload):

    time = datetime.now() + timedelta(seconds=data.countdown_second)
    print(time)
    task = create_task.apply_async(
        (data.countdown_second, data.x, data.y),
        countdown=data.countdown_second
    )
    return {
        "status": "ok",
        "task": task.task_id,
    }
