# default
import datetime, pytz

from peewee import CharField, IntegerField, DateTimeField, ForeignKeyField, BooleanField, ManyToManyField
from database.postgres.peewee.sync import PeeweeModel

from apps.news.models import Tags
from apps.authentication.models import Users


def vn_now():
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    pst_now = utc_now.astimezone(pytz.timezone("Asia/Ho_Chi_Minh"))
    now =  datetime.datetime(pst_now.year , pst_now.month , pst_now.day, pst_now.hour, pst_now.minute)
    # now = now.strftime('%Y-%m-%d')
    
    return now

class News(PeeweeModel):
    id = IntegerField(primary_key=True)

    view = IntegerField(default=0)
    rating = IntegerField(default=0)
    description = CharField()
    keywords = CharField()
    og_img = CharField(default="")
    title = CharField()
    content = CharField()
    created_at = DateTimeField(default=vn_now())
    created_by = ForeignKeyField(Users, backref="news")
    updated_at = DateTimeField(default=vn_now())
    updated_by = ForeignKeyField(Users, backref="news")
    thumbnail_img = CharField()
    banner_img = CharField(null=True)
    is_slideshow = BooleanField(default=False)
    tags = ManyToManyField(Tags, backref="news")

    class Meta:
        db_table = 'news'

    @classmethod
    def get_list(cls):
        query = cls.select().dicts()
        return list(query)

# NewsTags = News.tags.get_through_model()
# db.create_tables([NewsTags])
