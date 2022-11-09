from peewee import Model
import peewee_async
import logging
from all_env import POSTGRES_USER, POSTGRES_PASS, POSTGRES_DB, POSTGRES_PORT, POSTGRES_HOST

database = peewee_async.PostgresqlDatabase(
    POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PASS, host=POSTGRES_HOST, port=POSTGRES_PORT
)
db = peewee_async.Manager(database)
# db.database.allow_sync = False
# db.database.allow_sync = logging.ERROR

class PeeweeModel(Model):
    pass

    class Meta:
        database = database