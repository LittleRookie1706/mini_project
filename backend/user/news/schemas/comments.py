from typing import Optional, List
import datetime
from pydantic import BaseModel, Field
from models import vn_now
    

class CommentsSchema(BaseModel):
    id: int
    user: int
    news: int
    rating: int = Field(default=3)
    content: str = Field(max_length=10000)
    created_at: datetime.datetime = Field(default=vn_now())
    updated_at: datetime.datetime = Field(default=vn_now())