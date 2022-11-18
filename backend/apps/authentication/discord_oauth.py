# fastapi
from fastapi import Depends
from fastapi.responses import JSONResponse

#discord
from fastapi_discord import User, DiscordOAuthClient

#local
from . import router
from all_env import CLIENT_ID, CLIENT_SECRET, REDIRECT_URL
from .models import Users

discord = DiscordOAuthClient(
    CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, 
    ("identify", "guilds", "email")
)  # scopes

# start
@router.on_event("startup")
async def on_startup():
    await discord.init()


@router.get("/discord-oauth/{code}")
async def discord_oauth(code: str):
    token, refresh_token = await discord.get_access_token(code)
    return {"access_token": token, "refresh_token": refresh_token}

@router.get("/get-user/", dependencies=[Depends(discord.requires_authorization)])
async def get_user(discord_user: User = Depends(discord.user)):
    user = Users.get(discord_id=discord_user.id).__data__
    return user

@router.patch("/discord-users/{discord_id}", dependencies=[Depends(discord.requires_authorization)])
async def update_user(discord_id: str, user: User = Depends(discord.user)):
    if user.id == discord_id:
        query = Users.update(
            email=user.email,
            username=user.username,
            avatar=user.avatar_url,
            # is_admin=is_admin(int(user.id)),
        ).where(Users.discord_id==user.id)
        query.execute()
        return "oke"
    return JSONResponse({"error": "Permission denied"}, status_code=403)


