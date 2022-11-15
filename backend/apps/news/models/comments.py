# default
import datetime, pytz

# 
from peewee import CharField, IntegerField, DateTimeField, ForeignKeyField
from database.postgres.peewee.sync import PeeweeModel

#
from .news import News
from apps.authentication.models import Users

def vn_now():
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    pst_now = utc_now.astimezone(pytz.timezone("Asia/Ho_Chi_Minh"))
    now =  datetime.datetime(pst_now.year , pst_now.month , pst_now.day, pst_now.hour, pst_now.minute)
    
    return now

class Comments(PeeweeModel):
    id = IntegerField(primary_key=True)

    user = ForeignKeyField(Users, backref="comments")
    news = ForeignKeyField(News, backref="comments")
    rating = IntegerField(default=0)
    content = CharField(max_length=2000)
    created_at = DateTimeField(default=vn_now())
    updated_at = DateTimeField(default=vn_now())

    class Meta:
        db_table = 'comments'

    @classmethod
    def get_list(cls):
        query = cls.select().dicts()
        return list(query)

# NewsTags = News.tags.get_through_model()
# db.create_tables([NewsTags])
