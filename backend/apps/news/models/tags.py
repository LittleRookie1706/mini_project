from peewee import IntegerField, TextField

from database.postgres.peewee.sync import PeeweeModel

class Tags(PeeweeModel):
    id = IntegerField(primary_key=True)
    name = TextField()

    class Meta:
        db_table = 'tags'

    @classmethod
    def get_list(cls):
        query = cls.select().dicts()
        return list(query)