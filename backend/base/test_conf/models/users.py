from peewee import CharField, IntegerField, BooleanField

from . import PeeweeModel

class Users(PeeweeModel):

    id = IntegerField()

    email = CharField()
    username = CharField()
    avatar = CharField()
    is_admin = BooleanField(default=False)
    discord_id = CharField(null=True)

    class Meta:
        table_name = 'users'

    @classmethod
    def get_list(cls):
        query = cls.select().dicts()
        return list(query)
