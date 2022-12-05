# default
from typing import Optional
# import ast

# fastapi
from fastapi import HTTPException
# from fastapi_cache.decorator import cache

# local
from . import router
from models import News
    
    
@router.get("/news/")
# @cache(expire=3600)
async def get_news_by_page_number(
    page_number: Optional[int] = None, 
    is_slideshow: Optional[bool] = None, 
    order_by_view: Optional[bool] = None,
    tag: Optional[int] = None,
    ):
    if order_by_view:
        return News.get_most_view(10)
    elif is_slideshow:
        return News.get_slideshow_by_page(page_number)
    elif tag:
        return News.get_by_tag(tag, page_number)
    elif page_number:
        return News.get_by_page(page_number)

    raise HTTPException(detail={"error": "Invalid page_number"}, status_code=400)


@router.get("/news/{news_id}/")
# @cache(expire=3600)
async def get_news_by_page_number(news_id: int):
    news = News.get_or_none(id=news_id)
    if news:
        News.update(view=News.view+1).where(News.id==news.id).execute()
        news = news.__data__
        # news['content'] = ast.literal_eval(news['content'])
        return news
    raise HTTPException(detail={"error": "Not found news"}, status_code=404)


@router.get("/news/{news_id}/tags/")
async def get_news_by_page_number(news_id: int):
    news = News.get_or_none(id=news_id)
    if news:
        return News.get_tags(news_id)
    raise HTTPException(detail={"error": "Not found news"}, status_code=404)

