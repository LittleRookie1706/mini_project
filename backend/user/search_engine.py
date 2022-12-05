# 
from typing import Optional
# 
from fastapi import APIRouter
# 
from database.meilisearch.sync import news_index

router = APIRouter(
    prefix="/api",
    tags=["Search"],
    responses={404: {"description": "Not found"}},
)

@router.get('/search/{search_content}')
async def search(search_content: str, tag: Optional[int] = None):
    if tag:
        return news_index.search(search_content, {
            'filter': [f'tags = {tag}']
        })["hits"]
    else:
        return news_index.search(search_content)["hits"]