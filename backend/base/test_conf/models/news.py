# default
import datetime, pytz
from datetime import date

from peewee import CharField, IntegerField, DateTimeField, ForeignKeyField, BooleanField, ManyToManyField
from . import PeeweeModel

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
    og_img = CharField(null=True)
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
        table_name = 'news'

    # get news list
    @classmethod
    def get_list(cls):
        query = cls.select().dicts()
        return list(query)

    @classmethod
    def get_by_page(cls, page: int):
        start_point = (page-1) * 17
        end_point = page * 17
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
    def get_by_tag(cls, tag: int, page: int):
        start_point = (page-1) * 20
        end_point = page * 20
        news_list = [news["news"] for news in list(NewsTags.select(NewsTags.news_id).where(NewsTags.tags_id==tag).dicts())]
        query = (cls.select(News.id, News.view, News.rating, News.description, News.title, News.thumbnail_img, News.banner_img, News.is_slideshow)
                    .where(News.id.in_(news_list))
                    .order_by(News.id.desc())
                ).dicts()
        return list(query[start_point:end_point])

    # get single news
    @classmethod
    def get_tags(cls, news_id: int):
        news_tags = NewsTags.select(Tags.id, Tags.name).join(Tags).where(NewsTags.news_id==news_id).dicts()
        return list(news_tags)

    # statistic
    @classmethod
    def view_by_date(cls, start_date: date, end_date: date):
        return []

    @classmethod
    def view_by_tag(cls, start_date: date, end_date: date):
        tags = list(NewsTags.select().join(Tags).dicts())
        print(tags)
        return []

    @classmethod
    def avg_rate_by_tag(cls, start_date: date, end_date: date):
        return []

    @classmethod
    def rate_by_tag(cls, start_date: date, end_date: date):
        return []

NewsTags = News.tags.get_through_model()
# db.create_tables([NewsTags])

async def get_news(id: int):
    news = News.get_or_none(id=id)
    return news