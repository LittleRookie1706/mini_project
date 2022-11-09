# sql module
from sqlmodel import SQLModel, Field, Relationship

# local
from migrations.models import Users
from .news import News

class Comments(SQLModel, table=True):
    id: int = Field(primary_key=True)

    user_id: Users = Relationship()
    news_id: News = Relationship()
    rate: int = Field(default=0)
    comments: str = Field(max_length=2000)