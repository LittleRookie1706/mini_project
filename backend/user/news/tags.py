# default
from typing import List

# fastapi
from fastapi_cache.decorator import cache


# local
from . import router
from .schemas import TagsSchema
from models import Tags


@router.get("/tags/", response_model=List[TagsSchema])
# @cache(expire=3600)
async def list_tags():
    return Tags.get_list()
