from peewee import *
import datetime
from .model import TodoIn, TodoOut
db = SqliteDatabase('Todo.db')


class BaseModel(Model):
    class Meta:
        database = db


class Todo(BaseModel):
    id = AutoField()
    title = CharField(max_length=5000)
    status = CharField(max_length=5000)
    lastUpdate = DateTimeField(default=datetime.datetime.now)


def connectDb():
    global db
    db.connect()
    db.create_tables([Todo])


def addTodo(todoIn):
    todo = Todo.create(title=todoIn.title, status=todoIn.status)
    db.commit()
    return TodoOut(id=todo.id, title=todo.title, status=todo.status, lastUpdate=(todo.lastUpdate).strftime("%d/%m/%Y, %H:%M:%S"))


def updateTodo(id, todoIn):
    todo = Todo.select().where(Todo.id == id).get()
    todo.title = todoIn.title
    todo.status = todoIn.status
    todo.lastUpdate = datetime.datetime.now()
    todo.save()
    db.commit()
    return TodoOut(id=todo.id, title=todo.title, status=todo.status, lastUpdate=(todo.lastUpdate).strftime("%d/%m/%Y, %H:%M:%S"))


def commitData():
    db.commit()


def deleteTodo(id):
    todo = Todo.delete().where(Todo.id == id).execute()


def getAllTodos():
    todos = Todo.select()
    todoList = []
    for i in todos:
        todoList.append(TodoOut(id=i.id, title=i.title, status=i.status, lastUpdate=(
            i.lastUpdate).strftime("%d/%m/%Y, %H:%M:%S")))
    return todoList


def getSingleTodo(id):
    todo = Todo.select().where(Todo.id == id).get()
    return TodoOut(id=todo.id, title=todo.title, status=todo.status, lastUpdate=(todo.lastUpdate).strftime("%d/%m/%Y, %H:%M:%S"))
