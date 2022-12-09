from peewee import IntegerField, TextField, ForeignKeyField

from . import PeeweeModel

class TagGroups(PeeweeModel):
    id = IntegerField(primary_key=True)
    name = TextField(unique=True)

    class Meta:
        table_name = 'taggroups'

    @classmethod
    def get_list(cls):
        query = cls.select().dicts()
        return list(query)

class Tags(PeeweeModel):
    id = IntegerField(primary_key=True)
    name = TextField(unique=True)
    tag_group = ForeignKeyField(TagGroups, backref="tags")

    class Meta:
        table_name = 'tags'

    @classmethod
    def get_list(cls):
        query = (cls.select(Tags.id, Tags.name, TagGroups.name.alias('tag_group'))
            .join(TagGroups)
            .order_by(TagGroups.id.asc(), Tags.id.asc())).dicts()
        return list(query)

