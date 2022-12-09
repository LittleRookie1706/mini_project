from peewee import Model
from base.event_handle import db

class PeeweeModel(Model):
    pass
    class Meta:
        database = db

from .users import Users
from .news import News, NewsTags, vn_now
from .tags import Tags, TagGroups
from .comments import Comments