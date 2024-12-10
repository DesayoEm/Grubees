from sqlalchemy import Column, String, Boolean, Date, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from schemas.user_enums import GenderEnum, CountryEnum
from datetime import datetime, UTC, date
from typing import List, Optional


class Base(DeclarativeBase):
    pass

class Post(Base):
    __tablename__ = 'posts'
    #Essential fields