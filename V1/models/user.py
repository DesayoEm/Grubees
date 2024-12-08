from sqlalchemy import Column, Integer, String, Boolean, Text,\
    ARRAY, ForeignKey, Date, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from data.database import Base
from schemas.user_enums import GenderEnum, CountryEnum
from datetime import datetime, UTC

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    username = Column (String(20), unique = True, nullable = False)
    full_name = Column (String(50), nullable = False)
    email_address = Column (String(120), unique = True, nullable = False)
    password = Column (String(255), nullable = False)
    date_of_birth = Column (Date, nullable = False)
    bio = Column (String(300), nullable = True)
    avatar = Column (String(255), nullable = True)
    gender = Column(Enum(GenderEnum), nullable = True)
    phone = Column (String(15), nullable = True)
    country = Column(Enum(CountryEnum), nullable = True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(UTC), nullable=False)
    last_updated = Column(DateTime(timezone=True), default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC), nullable=False)
    posts =  relationship("Post", back_populates="user", cascade="all, delete-orphan")
    is_active = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    is_public = Column(Boolean, default=True, nullable=False)


    # def __repr__(self):
    #     return f"<User {self.username}>"

# __table_args__ = (
#     Index('ix_users_email_address', 'email_address'),
#     Index('ix_users_username', 'username'),
# )
#will help with query performance and data integrity.

# Used lambda for the datetime defaults to esure the timestamp is generated at record
# creation/update time rather than at class definition time.
# This is a more robust approach.