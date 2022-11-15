# fastapi
from fastapi import Depends, HTTPException

#local
from . import router
from apps.authentication.discord_oauth import discord
from fastapi_discord import User
from apps.authentication.models import Users
from apps.news.models import News, Tags
from apps.news.schemas import NewsSchema

def is_slideshow(banner_img):
    if banner_img in ["", None]:
        return False
    return True

@router.post("/news", response_model=NewsSchema, dependencies=[Depends(discord.requires_authorization)])
async def post_news(news: NewsSchema, user: User = Depends(discord.user)):
    user = Users.get(discord_id=user.id)
    if user.is_admin:
        print(news.__dict__)
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
            tags=[],
        )
        newsmodel.tags.add([ Tags.get(Tags.id == x) for x in news.tags ])
        return news
    else:
        return HTTPException(detail={"error": "Permission denied"}, status_code=403)

# @router.patch("/news", response_model=NewsSchema, dependencies=[Depends(discord.requires_authorization)])
# async def post_news(news: NewsSchema, user: User = Depends(discord.user)):
#     user = Users.get(discord_id=user.id)
#     if user.is_admin:
        # newsmodel = News.update(
        #     description=news.description,
        #     keywords=news.keywords,
        #     og_img=news.og_img,
        #     title=news.title,
        #     content=news.content,
        #     thumbnail_img=news.thumbnail_img,
        #     banner_img=news.banner_img,
        #     is_slideshow=is_slideshow(news.banner_img),

        #     created_by=user,
        #     updated_by=user,
        #     tags=[],
        # ).where(News.id)
        # newsmodel.tags.add([ Tags.get(Tags.id == x) for x in news.tags ])
        # return news
#     else:
#         return HTTPException(detail={"error": "Permission denied"}, status_code=403)