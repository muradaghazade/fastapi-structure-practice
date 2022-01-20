import peewee
import datetime
from config.database import db


class Todo(peewee.Model):
    title = peewee.CharField()
    description = peewee.TextField()
    created = peewee.DateTimeField(default=datetime.datetime.now)
    

    class Meta:
        database = db