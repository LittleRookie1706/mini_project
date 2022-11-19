from peewee import IntegerField, TextField, ForeignKeyField

from database.postgres.peewee.sync import PeeweeModel
from .taggroups import TagGroups

class Tags(PeeweeModel):
    id = IntegerField(primary_key=True)
    name = TextField(unique=True)
    tag_group = ForeignKeyField(TagGroups, backref="tags")

    class Meta:
        db_table = 'tags'

    @classmethod
    def get_list(cls):
        query = cls.select().dicts()
        return list(query)