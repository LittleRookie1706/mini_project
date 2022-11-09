# fastapi
from fastapi import Depends

#discord
from fastapi_discord import User, DiscordOAuthClient


#local
from . import router

from all_env import CLIENT_ID, CLIENT_SECRET, REDIRECT_URL
from .models import Users
from database.postgres.peewee_async import db

admin_ids=[]

discord = DiscordOAuthClient(
    CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, 
    ("identify", "guilds", "email")
)  # scopes

def is_admin(user_id: int) -> bool:
    if user_id in admin_ids:
        return True
    else:
        return False

# start
@router.on_event("startup")
async def on_startup():
    await discord.init()


@router.get("/discord-oauth")
async def discord_oauth(code: str):
    token, refresh_token = await discord.get_access_token(code)
    return {"access_token": token, "refresh_token": refresh_token}

@router.get("/get-user", dependencies=[Depends(discord.requires_authorization)])
async def get_user(user: User = Depends(discord.user)):
    return await db.get(Users, discord_id=user.id)

@router.put("/user", dependencies=[Depends(discord.requires_authorization)])
async def update_user(user: User = Depends(discord.user)):

    await db.get_or_create(Users,
        email=user.email,
        username=user.username,
        avatar=user.avatar_url,
        discord_id=str(user.id)
    )

    return await db.get(Users, discord_id=user.id)

