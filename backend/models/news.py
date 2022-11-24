# default
import datetime, pytz

from fastapi import HTTPException

from peewee import CharField, IntegerField, DateTimeField, ForeignKeyField, BooleanField, ManyToManyField
from database.postgres.peewee.sync import PeeweeModel

from .tags import Tags
from .users import Users


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

    @classmethod
    def get_by_page(cls, page: int):
        start_point = (page-1) * 20
        end_point = page * 20
        query = cls.select(News.id, News.view, News.rating, News.description, News.title, News.thumbnail_img, News.banner_img, News.is_slideshow).order_by(News.id.desc()).dicts()
        return list(query[start_point:end_point])

    @classmethod
    def get_most_view(cls, num: int):
        query = cls.select(News.id, News.view, News.rating, News.description, News.title, News.thumbnail_img, News.banner_img, News.is_slideshow).order_by(News.view.desc(), News.id.desc()).limit(num).dicts()
        return list(query)

    @classmethod
    def get_slideshow_by_page(cls, page: int):
        start_point = (page-1) * 4
        end_point = page * 4
        query = cls.select(News.id, News.view, News.rating, News.description, News.title, News.thumbnail_img, News.banner_img, News.is_slideshow).where(News.is_slideshow == True).order_by(News.id.desc()).dicts()
        return list(query[start_point:end_point])

    @classmethod
    def get_tags(cls, news_id: int):
        news_tags = NewsTags.select(Tags.id, Tags.name).join(Tags).where(NewsTags.news_id==news_id).dicts()
        return list(news_tags)

NewsTags = News.tags.get_through_model()
# db.create_tables([NewsTags])
