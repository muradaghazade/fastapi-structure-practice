from fastapi import FastAPI, Depends
from routers import todo
from config import database
from models.todo import Todo

app = FastAPI()

app.include_router(todo.router)