from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse


app = FastAPI()

tasks = []

class Task(BaseModel):
    name: str

@app.get("/")
def read_root():
    return FileResponse("static/index.html")

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

@app.put('/update-task/{task_id}')
def update_task(task_id: int, task: Task):
    if task_id < 0 or task_id >= len(tasks):
        return { 'msg': 'Task not found' }
    tasks[task_id] = task
    return { 'msg': 'Task updated succesfully' }

@app.delete('/delete-task/{task_id}')
def delete_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        return { 'msg': 'Task not found' }
    tasks.pop(task_id)
    return { 'msg': 'Task deleted succesfully' }