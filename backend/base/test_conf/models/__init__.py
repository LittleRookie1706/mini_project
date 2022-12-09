import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents[2] 
sys.path.append(str(package_root_directory))
# 

import peewee
from peewee import Model
from contextvars import ContextVar
from all_env import POSTGRES_USER, POSTGRES_PASS, POSTGRES_DB, POSTGRES_PORT, POSTGRES_HOST

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

db = peewee.PostgresqlDatabase(
        f"{POSTGRES_DB}_test", user=POSTGRES_USER, password=POSTGRES_PASS, host=POSTGRES_HOST, port=POSTGRES_PORT
    )

db._state = PeeweeConnectionState()


class PeeweeModel(Model):
    pass
    class Meta:
        database = db

from .users import Users
from .news import News, NewsTags, vn_now
from .tags import Tags, TagGroups
from .comments import Comments