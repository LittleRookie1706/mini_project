# default
from typing import List

# fastapi
from fastapi import Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

# local
from . import router
# from .schemas import News


# # news_title: str, 
# @router.get("/news", response_model=List[News])
# async def post_content():
#     pass

# @router.post("/songs")
# async def add_song(news: News, session: AsyncSession = Depends(get_session)):
#     news = News(name=news.name, artist=news.artist)
#     session.add(news)
#     await session.commit()
#     await session.refresh(news)
#     return news