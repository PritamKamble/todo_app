from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tasks = []

class Task(BaseModel):
    name: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello123")
def hello():
    return { 'msg': 'Hello from hello 123' }

@app.post('/create-task')
def create_task(task: Task):
    print(task)
    tasks.append(task)
    return { 'msg': 'Task added succesfully'}


@app.get('/get-tasks')
def get_tasks():
    return { "tasks": tasks }


