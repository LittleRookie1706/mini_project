# fastapi
from fastapi import HTTPException, Depends
from fastapi.responses import JSONResponse
from user.authentication.discord_oauth import discord
from fastapi_discord import User
from peewee import IntegrityError

# local
from . import router
from models import News, Comments, Users
from .schemas import CommentsSchema

@router.get("/news/{news_id}/comments/")
async def get_comments_by_news_id(news_id: int):
    news = News.get_or_none(id=news_id)
    if news:
        return Comments.get_news_comments(news_id)
    raise HTTPException(detail={"error": "Not found news"}, status_code=404)
    

@router.post("/news/comments/", dependencies=[Depends(discord.requires_authorization)], status_code=201)
async def post_comments(comment: CommentsSchema, user: User = Depends(discord.user)):
    try:
        user = Users.get_or_none(Users.discord_id==user.id)
        news = News.get_or_none(News.id==comment.news)
        comment = Comments.create(
            user = user,
            news = news,
            rating = comment.rating,
            content = comment.content,
        )
        return JSONResponse(comment.__data__, status_code=201)
    except IntegrityError:
        raise HTTPException(detail={"error": "Not found news"}, status_code=404)

# @router.patch("/comments/{comment_id}", response_model=CommentsSchema, dependencies=[Depends(discord.requires_authorization)])
# async def get_news_by_page_number(comment: CommentsSchema, user: User = Depends(discord.user)):
#     user = Users.get_or_none(Users.discord_id==user.id)
#     Comments.create(
#         user = user.id,
#         news = comment.news,
#         rating = comment.rating,
#         comment = comment.content,
#     )
#     return comment