from typing import Optional, List
from pydantic import BaseModel, Field
    

class NewsSchema(BaseModel):
    id: int
    view: int = Field(default=0)
    rating: int = Field(default=0)
    description: str
    keywords: str
    og_img: Optional[str]
    title: str
    content: str
    thumbnail_img: str = Field(default="")
    banner_img: Optional[str]
    is_slideshow: bool = Field(default=False)
    tags: List[int]
