from database.postgres.peewee.sync import PeeweeModel
from peewee import CharField, IntegerField, DateTimeField, ForeignKeyField

from models import Users, News, vn_now

class Comments(PeeweeModel):
    id = IntegerField(primary_key=True)

    user = ForeignKeyField(Users, backref="comments")
    news = ForeignKeyField(News, backref="comments")
    rating = IntegerField(default=3)
    content = CharField(max_length=10000)
    created_at = DateTimeField(default=vn_now())
    updated_at = DateTimeField(default=vn_now())

    class Meta:
        db_table = 'comments'

    @classmethod
    def get_news_comments(cls, news_id):
        comments = (Comments
            .select(Comments.id, Comments.rating, Comments.content, Comments.created_at, Comments.updated_at, Users.id, Users.username, Users.avatar)
            .join(Users)
            .where(Comments.news==news_id).dicts())

        return list(comments)
