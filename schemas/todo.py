from typing import List, Optional, Any
from datetime import datetime
import peewee
from pydantic import BaseModel
from pydantic.utils import GetterDict


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


class TodoBase(BaseModel):
    title: str
    description:str


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    id: int
    created: datetime

    class Config:
        orm_mode = True