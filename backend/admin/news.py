# default
from typing import Optional, Union, List
import aiofiles
from random import randrange
# fastapi
from fastapi import Depends, HTTPException, File, UploadFile, Form
from fastapi.responses import JSONResponse

#local
from . import router
from user.authentication.discord_oauth import discord
from fastapi_discord import User
from models import Users, News, Tags, vn_now
from user.news.schemas import NewsSchema, PostNewsSchema, PatchNewsSchema
from database.imgbb.sync import upload_imgbb_image, async_delete_image, delete_image

def is_slideshow(banner_img):
    if banner_img in ["", None]:
        return False
    return True

async def img_handle(file: File):
    file_direct = f'media/{file.filename}-{randrange(1000000)}.png'
    async with aiofiles.open(file_direct, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)
    link = upload_imgbb_image(file_direct)
    delete_image(file_direct)
    return link

async def img_save(thumbnail_img: File, og_img: Optional[File] = None, banner_img: Optional[File] = None):
    if thumbnail_img:
        thumbnail_img = await img_handle(thumbnail_img)
    if og_img:
        og_img = await img_handle(og_img)
    if banner_img:
        banner_img = await img_handle(banner_img)

    return {
        'thumbnail_img': thumbnail_img,
        'og_img': og_img,
        'banner_img': banner_img
    }

@router.post("/news/", dependencies=[Depends(discord.requires_authorization)])
async def post_news(
        description: str = Form(),
        keywords: str = Form(),
        title: str = Form(),
        content: str = Form(),
        tags: List[int] = Form(),
        thumbnail_img: UploadFile = File(),
        og_img: Union[UploadFile, None] = None,
        banner_img: Union[UploadFile, None] = None,
        user: User = Depends(discord.user)
    ):
    
    user = Users.get(discord_id=user.id)
    if user.is_admin:
        files = await img_save(thumbnail_img, og_img, banner_img)
        files_exclude = {key: value for key, value in files.items() if value}
        newsmodel = News.create(
            description= description,
            keywords= keywords,
            title= title,
            content= content,
            tags= tags,
            **files_exclude,
            is_slideshow=is_slideshow(files['banner_img']),
            created_by=user,
            updated_by=user,
        )
        newsmodel.tags.add([ Tags.get(Tags.id == x) for x in tags ])
        return newsmodel.__data__
    else:
        raise HTTPException(detail={"error": "Permission denied"}, status_code=403)

@router.patch("/news/{news_id}", dependencies=[Depends(discord.requires_authorization)])
async def patch_news(
        news_id: int, 
        description: Optional[str] = Form(default=None),
        keywords: Optional[str] = Form(default=None),
        title: Optional[str] = Form(default=None),
        content: Optional[str] = Form(default=None),
        tags: Optional[List[int]] = Form(default=None),
        thumbnail_img: Union[UploadFile, None] = None,
        og_img: Union[UploadFile, None] = None,
        banner_img: Union[UploadFile, None] = None,
        user: User = Depends(discord.user)
    ):
    
    user = Users.get(discord_id=user.id)
    if user.is_admin:
        old_newsmodel=News.get_or_none(id=news_id)
        if old_newsmodel:
            files = await img_save(thumbnail_img, og_img, banner_img)
            values = {'description': description, 'keywords': keywords, 'title': title, 'content': content, 'tags': tags}
            update_values = {key: value for key, value in files.items() if value}
            update_values.update({key: value for key, value in values.items() if value})
            print(update_values)

            if tags:
                old_newsmodel.tags.clear()
                old_newsmodel.tags.add([ Tags.get(Tags.id == x) for x in tags ])
                del update_values['tags']

            newsmodel = News.update(
                update_values,
                is_slideshow=is_slideshow(files['banner_img']),
                updated_by=user,
                updated_at=vn_now(),
            ).where(News.id==news_id)
            newsmodel.execute()

            return update_values

        raise HTTPException(detail={"error": "News does not excist"}, status_code=404)
    else:
        raise HTTPException(detail={"error": "Permission denied"}, status_code=403)

@router.delete("/news/{news_id}", dependencies=[Depends(discord.requires_authorization)])
async def delete_news(news_id: int, user: User = Depends(discord.user)):
    user = Users.get(discord_id=user.id)
    if user.is_admin:
        old_newsmodel=News.get_or_none(id=news_id)
        if old_newsmodel:
            old_newsmodel.delete_instance(recursive=True)
            return JSONResponse({"status": "success"}, status_code=200)
        raise HTTPException(detail={"error": "News does not excist"}, status_code=404)
    else:
        raise HTTPException(detail={"error": "Permission denied"}, status_code=403)

