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

# class News(SQLModel, table=True):
#     id: int = Field(primary_key=True)

#     view: int = Field(default=0)
#     rating: int = Field(default=0)
#     description: str = Field()
#     keywords: str = Field()
#     og_img: str = Field(default="")
#     title: str = Field()
#     content: str = Field()
#     created_at: datetime.datetime = Field(default=vn_now())
#     created_by: Users = Relationship()
#     updated_at: datetime.datetime = Field(default=vn_now())
#     updated_by: Users = Relationship()
#     thumbnail_img: str = Field(default="")
#     banner_img: str = Field(nullable=True)
#     is_slideshow: bool = Field(default=False)
#     tag: List["Tags"] = Relationship()
