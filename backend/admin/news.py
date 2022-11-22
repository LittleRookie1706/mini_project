# fastapi
from fastapi import Depends, HTTPException
from fastapi.responses import JSONResponse

#local
from . import router
from user.authentication.discord_oauth import discord
from fastapi_discord import User
from models import Users, News, Tags, vn_now
from user.news.schemas import NewsSchema

def is_slideshow(banner_img):
    if banner_img in ["", None]:
        return False
    return True

@router.post("/news/", response_model=NewsSchema, dependencies=[Depends(discord.requires_authorization)])
async def post_news(news: NewsSchema, user: User = Depends(discord.user)):

    user = Users.get(discord_id=user.id)
    if user.is_admin:
        newsmodel = News.create(
            description=news.description,
            keywords=news.keywords,
            og_img=news.og_img,
            title=news.title,
            content=news.content,
            thumbnail_img=news.thumbnail_img,
            banner_img=news.banner_img,
            is_slideshow=is_slideshow(news.banner_img),

            created_by=user,
            updated_by=user,
        )
        newsmodel.tags.add([ Tags.get(Tags.id == x) for x in news.tags ])
        return news
    else:
        raise HTTPException(detail={"error": "Permission denied"}, status_code=403)

@router.patch("/news/{news_id}", response_model=NewsSchema, dependencies=[Depends(discord.requires_authorization)])
async def post_news(news_id: int, news: NewsSchema, user: User = Depends(discord.user)):
    user = Users.get(discord_id=user.id)
    if user.is_admin:
        old_newsmodel=News.get_or_none(id=news_id)
        if old_newsmodel:
            newsmodel = News.update(
                description=news.description,
                keywords=news.keywords,
                og_img=news.og_img,
                title=news.title,
                content=news.content,
                thumbnail_img=news.thumbnail_img,
                banner_img=news.banner_img,
                is_slideshow=is_slideshow(news.banner_img),

                updated_by=user,
                updated_at=vn_now(),
            ).where(News.id==news_id)
            newsmodel.execute()
            old_newsmodel.tags.clear()
            old_newsmodel.tags.add([ Tags.get(Tags.id == x) for x in news.tags ])
            
            return news

        raise HTTPException(detail={"error": "News does not excist"}, status_code=404)
    else:
        raise HTTPException(detail={"error": "Permission denied"}, status_code=403)

@router.delete("/news/{news_id}", dependencies=[Depends(discord.requires_authorization)])
async def post_news(news_id: int, user: User = Depends(discord.user)):
    user = Users.get(discord_id=user.id)
    if user.is_admin:
        old_newsmodel=News.get_or_none(id=news_id)
        if old_newsmodel:
            old_newsmodel.delete_instance(recursive=True)
            return JSONResponse({"status": "success"}, status_code=200)
        raise HTTPException(detail={"error": "News does not excist"}, status_code=404)
    else:
        raise HTTPException(detail={"error": "Permission denied"}, status_code=403)