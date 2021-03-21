from typing import Optional

from fastapi import FastAPI
from helper.model import *
from helper.db import *
app = FastAPI()


@app.get("/")
def get_all_todos():
    return getAllTodos()


@app.get("/todo/{id}")
def get_single_todo(id: int):
    return getSingleTodo(id)


@app.post("/todo")
def add_todo(todo: TodoIn):
    return addTodo(todo)


@app.put("/todo/{id}")
def update_todo(id: int, todo: TodoIn):
    return updateTodo(id, todo)


@app.delete("/todo/{id}")
def delete_todo(id: int):
    todo = getSingleTodo(id)
    deleteTodo(id)
    return todo


@app.on_event("startup")
async def startup_event():
    connectDb()
