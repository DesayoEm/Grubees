from pydantic import BaseModel,EmailStr
from uuid import UUID
from datetime import datetime,date
from schemas.posts import Posts

class UserBase(BaseModel):
    id:UUID
    username:str
    full_name:str
    phone:str
    email_address: EmailStr
    password:str
    date_of_birth: date
    bio:str | None = None
    avatar:str| None = None


class User(UserBase):
    created_at:datetime
    last_updated:datetime
    posts:list[str]=[]
    is_active:bool = False
    is_verified:bool = False

class UserUpdate(UserBase):
    pass