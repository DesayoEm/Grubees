from pydantic import BaseModel,EmailStr, field_validator
from user_enums import CountryEnum, GenderEnum
from uuid import UUID
from datetime import datetime,date
from starlette.authentication import BaseUser
from schemas.posts import Posts

class Login(BaseModel):
    input_value: str
    password:str

# @validator('phone_number')
# def validate_phone(cls, value):
#     # Remove any spaces or dashes
#     num = ''.join(filter(str.isdigit, value))
#     if not num.isdigit():
#         raise ValueError('Phone number must contain only digits')
#     if not 10 <= len(num) <= 15:  # Common lengths for phone numbers globally
#         raise ValueError('Invalid phone number length')
#     return num
class NewUser(BaseModel):
    id:UUID
    username:str
    full_name:str
    email_address: EmailStr
    password:str
    date_of_birth: date

class UserProfile(BaseModel):
    #public profile
    username:str
    full_name:str
    bio:str | None = None
    avatar:str| None = None

class UserAccount(UserProfile):
    #account details and settings
    gender:GenderEnum
    phone:str
    country:CountryEnum



class UserInfo(BaseUser):
    #for internal data
    created_at:datetime
    last_updated:datetime
    posts:list[str]=[]
    is_active:bool = False
    is_verified:bool = False
    is_public:bool = True

class ProfileUpdate(UserProfile):
    pass

class AccountUpdate(UserAccount):
    pass

class PasswordChange(BaseModel):
    current_password: str
    new_password: str
    confirm_password: str


#
# @validator('phone_number')
# def validate_phone(cls, value):
#     # Remove any spaces or dashes
#     num = ''.join(filter(str.isdigit, value))
#     if not num.isdigit():
#         raise ValueError('Phone number must contain only digits')
#     if not 10 <= len(num) <= 15:  # Common lengths for phone numbers globally
#         raise ValueError('Invalid phone number length')
#     return num