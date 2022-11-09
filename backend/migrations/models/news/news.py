# default
from typing import List
import datetime, pytz

# sql module
from sqlmodel import SQLModel, Field, Relationship
from ..authentication import Users

def vn_now():
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    pst_now = utc_now.astimezone(pytz.timezone("Asia/Ho_Chi_Minh"))
    now =  datetime.datetime(pst_now.year , pst_now.month , pst_now.day, pst_now.hour, pst_now.minute)
    
    return now


class Tags(SQLModel, table=True):
    id: int = Field(primary_key=True)

    name: str = Field()


class News(SQLModel, table=True):
    id: int = Field(primary_key=True)

    view: int = Field(default=0)
    rating: int = Field(default=0)
    description: str = Field()
    keywords: str = Field()
    og_img: str = Field(default="")
    title: str = Field()
    content: str = Field()
    created_at: datetime.datetime = Field(default=vn_now())
    created_by: Users = Relationship()
    updated_at: datetime.datetime = Field(default=vn_now())
    updated_by: Users = Relationship()
    thumbnail_img: str = Field(default="")
    banner_img: str = Field(nullable=True)
    is_slideshow: bool = Field(default=False)
    tag: List["Tags"] = Relationship()
