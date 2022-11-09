from typing import Optional
from pydantic import BaseModel
    
class PostContent(BaseModel):

    count: int
    position: int

    description: str
    keywords: str #should be list
    og_image: Optional[str]
    title: str
    content: str

    date: list
    name: str
    html_type: str
    thumbnail_link: str
    slide_show_link: str

    rate: int
    view: int
    tags: list



class MinimumPostContent(BaseModel):
    position: int
    name: str
    title: str
    description: str
    thumbnail_link: str
    slide_show_link: str
