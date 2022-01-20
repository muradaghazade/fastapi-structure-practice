from contextvars import ContextVar

import peewee

DATABASE_NAME = "test.db"
db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


# db = peewee.SqliteDatabase(DATABASE_NAME, check_same_thread=False)
# db = peewee.MySQLDatabase(
#         "mysql",user="root",
#         password="password",port=3306
#     )

db = peewee.PostgresqlDatabase('test_db', user='user', password='12345',
                           host='127.0.0.1', port=5432)


db._state = PeeweeConnectionState()