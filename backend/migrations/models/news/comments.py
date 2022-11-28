import datetime, pytz
from typing import Optional
# sql module
from sqlmodel import SQLModel, Field


def vn_now():
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    pst_now = utc_now.astimezone(pytz.timezone("Asia/Ho_Chi_Minh"))
    now =  datetime.datetime(pst_now.year , pst_now.month , pst_now.day, pst_now.hour, pst_now.minute)
    
    return now
class Comments(SQLModel, table=True):
    id: int = Field(primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="users.id")
    news_id: Optional[int] = Field(default=None, foreign_key="news.id")
    rating: int = Field(default=0)
    content: str = Field(max_length=2000)
    created_at: datetime.datetime = Field(default=vn_now())
    updated_at: datetime.datetime = Field(default=vn_now())
