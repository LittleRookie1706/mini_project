# default
from typing import Optional, List
import datetime, pytz

# sql module
from sqlmodel import SQLModel, Field, Relationship
from .tags import Tags

def vn_now():
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    pst_now = utc_now.astimezone(pytz.timezone("Asia/Ho_Chi_Minh"))
    now =  datetime.datetime(pst_now.year , pst_now.month , pst_now.day, pst_now.hour, pst_now.minute)
    
    return now

class News_Tags_Through(SQLModel, table=True):
    id: int = Field(primary_key=True)
    news_id: Optional[int] = Field(default=None, foreign_key="news.id")
    tags_id: Optional[int] = Field(default=None, foreign_key="tags.id")



class News(SQLModel, table=True):
    id: int = Field(primary_key=True)
    view: int = Field(default=0)
    rating: int = Field(default=0)
    description: str = Field()
    keywords: str = Field()
    og_img: str = Field(nullable=True)
    title: str = Field(unique=True)
    content: str = Field()
    created_at: datetime.datetime = Field(default=vn_now())
    created_by_id: Optional[int] = Field(default=None, foreign_key="users.id")
    updated_at: datetime.datetime = Field(default=vn_now())
    updated_by_id: Optional[int] = Field(default=None, foreign_key="users.id")
    thumbnail_img: str = Field()
    banner_img: str = Field(nullable=True)
    is_slideshow: bool = Field(default=False)
    tags: List["Tags"] = Relationship(back_populates="tags.id")
