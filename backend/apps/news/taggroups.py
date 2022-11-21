# default
from typing import List

# local
from . import router
from .schemas import TagsSchema
from .models import Tags


@router.get("/tags/", response_model=List[TagsSchema])
async def list_tags():
    return Tags.get_list()
    
