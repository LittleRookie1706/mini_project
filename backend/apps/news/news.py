# local
from . import router
from .models import News

@router.get("/news")
async def get_news():
    return News.select().count()

