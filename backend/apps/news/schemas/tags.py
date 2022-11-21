from typing import Optional

from pydantic import BaseModel

class TagsSchema(BaseModel):
    id: int
    name: str
    tag_group: Optional[str]

class TagGroupsSchema(BaseModel):
    id: int
    name: str