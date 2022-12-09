# default
from datetime import date
from typing import Union
# fastapi
from fastapi import Depends, HTTPException
# local
from . import router
from user.authentication.discord_oauth import discord
from fastapi_discord import User
from models import Users, News, Tags, vn_now


@router.get("/statistic", dependencies=[Depends(discord.requires_authorization)])
async def statistic(
        start_date: date, end_date: date, time_range: str, 
        view_by_date: bool, 
        view_by_tag: bool, 
        avg_rate_by_tag: bool, 
        rate_by_tag: bool, 
        user: User = Depends(discord.user)
    ):

    user = Users.get_or_none(discord_id=user.id)
    if user.is_admin:
        
        data_func = [
            (view_by_date, News.view_by_date),
            (view_by_tag, News.view_by_tag),
            (avg_rate_by_tag, News.avg_rate_by_tag),
            (rate_by_tag, News.rate_by_tag)
        ]

        result = []
        for data in data_func:
            if data[0]:
                result.append(data[1](start_date, end_date))

        return result
    raise HTTPException(detail={"error": "Permission denied"}, status_code=403)