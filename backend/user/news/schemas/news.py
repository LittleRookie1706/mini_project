from typing import Optional, List
import  datetime
from pydantic import BaseModel, Field
    
class NewsSchema(BaseModel):
    id: int
    view: int
    rating: int
    description: str
    keywords: str
    title: str
    content: str
    created_at: datetime.datetime
    created_by: int
    updated_at: datetime.datetime
    updated_by: int
    thumbnail_img: str
    banner_img: str
    is_slideshow: bool
    tags: List[int]
class PostNewsSchema(BaseModel):
    description: str
    keywords: str
    title: str
    content: str
    tags: List[int]


class PatchNewsSchema(BaseModel):
    description: Optional[str]
    keywords: Optional[str]
    title: Optional[str]
    content: Optional[str]
    tags: Optional[List[int]]
