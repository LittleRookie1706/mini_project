# default
from typing import List
# local
from . import router
from .models import News

# @router.get("/news")
# async def get_news():
#     return News.get_list()
    
@router.get("/news{page_number}")
async def get_news_by_page_number(page_number: int):
    return News.get_by_page(page_number)


@router.get("/most-view/")
async def get_news_by_page_number():
    return News.get_most_view(10)


@router.get("/slideshow{page_number}")
async def get_news_by_page_number(page_number: int):
    return News.get_slideshow_by_page(page_number)