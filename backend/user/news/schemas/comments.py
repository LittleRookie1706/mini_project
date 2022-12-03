from typing import Optional, List
import datetime
from pydantic import BaseModel, Field
from models import vn_now
    

class CommentsSchema(BaseModel):
    news: int
    rating: int = Field(default=3)
    content: str = Field(max_length=10000)