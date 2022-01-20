import schemas.todo as schemas
from models.todo import Todo


class TodoCRUD:
    def create_item(self, todo: schemas.TodoCreate):
        todo = Todo(title=todo.title, description=todo.description)
        todo.save()
        return todo

    def get_item(self, todo_id: int) -> schemas.Todo:
        todo = Todo.filter(schemas.Todo.id == todo_id).first()
        if todo:
            return todo
        return {"Detail": "Todo not found"}

    def get_items(self):
        return list(Todo.select())
