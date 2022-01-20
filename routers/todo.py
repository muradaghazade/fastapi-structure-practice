from fastapi import APIRouter
from models.todo import Todo
from services.todo_crud import TodoCRUD
from fastapi import Depends
from schemas import todo as schemas
from config import database
from typing import List

database.db.connect()
database.db.create_tables([Todo])
database.db.close()

router = APIRouter(prefix="/todo")

async def reset_db_state():
    database.db._state._state.set(database.db_state_default.copy())
    database.db._state.reset()


def get_db(db_state=Depends(reset_db_state)):
    try:
        database.db.connect()
        yield
    finally:
        if not database.db.is_closed():
            database.db.close()

crud = TodoCRUD()

@router.post('/todos/', response_model=schemas.Todo, dependencies=[Depends(get_db)], tags=["todos"])
def create_todo(todo: schemas.TodoCreate):
    return crud.create_item(todo=todo)


@router.get('/todos/', response_model=List[schemas.Todo], dependencies=[Depends(get_db)], tags=["todos"])
def create_todo():
    return crud.get_items()