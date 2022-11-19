from peewee import IntegerField, TextField

from database.postgres.peewee.sync import PeeweeModel

class TagGroups(PeeweeModel):
    id = IntegerField(primary_key=True)
    name = TextField(unique=True)

    class Meta:
        db_table = 'taggroups'

    @classmethod
    def get_list(cls):
        query = cls.select().dicts()
        return list(query)