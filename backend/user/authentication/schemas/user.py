from typing import Optional

from pydantic import BaseModel, EmailStr

class UsersSchema(BaseModel):
    id: int
    email: EmailStr
    name: str 
    avatar: str
    discord_id: Optional[str]
