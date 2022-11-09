from sqlmodel import SQLModel, Field
from pydantic import EmailStr

class Users(SQLModel, table=True):

    id: int = Field(primary_key=True)

    email: EmailStr = Field()
    username: str = Field()
    avatar: str = Field(default='')
    is_admin: bool = Field(default=False)
    discord_id: str = Field(default=None, unique=True)
    