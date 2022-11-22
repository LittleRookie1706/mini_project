# default
from typing import Optional

# fastapi
from fastapi import HTTPException

# local
from . import router
from models import News
    
    
@router.get("/news")
async def get_news_by_page_number(page_number: Optional[int] = None, is_slideshow: Optional[bool] = None, order_by_view: Optional[bool] = None):
    if order_by_view:
        return News.get_most_view(10)
    elif is_slideshow:
        return News.get_slideshow_by_page(page_number)
    elif page_number:
        return News.get_by_page(page_number)

    raise HTTPException(detail={"error": "Invalid page_number"}, status_code=400)