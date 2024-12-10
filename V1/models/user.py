from sqlalchemy import String, Boolean, Date, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from V1.schemas.posts import Posts
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from V1.schemas.user_enums import GenderEnum, CountryEnum
from datetime import datetime, UTC, date
from typing import List, Optional


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    #Essential fields
    id: Mapped[UUID] = mapped_column(UUID(as_uuid = True), primary_key=True, default = uuid4)
    username: Mapped[str] = mapped_column(String(20), unique = True, nullable = False)
    email_address: Mapped[str] = mapped_column (String(120), unique = True, nullable = False)
    password: Mapped[str] = mapped_column (String(255), nullable = False)

    #Profile information
    full_name: Mapped[str] = mapped_column (String(50), nullable = False)
    date_of_birth: Mapped[date] = mapped_column (Date, nullable = False)
    bio: Mapped[Optional[str]] = mapped_column(String(300))
    avatar: Mapped[Optional[str]] = mapped_column(String(255))
    gender: Mapped[Optional[GenderEnum]] = mapped_column(String(15))
    phone: Mapped[Optional[str]] = mapped_column(Enum(GenderEnum))
    country: Mapped[Optional[CountryEnum]] = mapped_column(Enum(CountryEnum), nullable = True)

    #Status flags
    is_active: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_public:Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    #Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False
    )
    last_updated: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        nullable=False
    )

    #relationships
    posts: Mapped[List["Posts"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )
    def __repr__(self):
        return f"<User {self.username}>"


# print(Base.metadata.tables)


# __table_args__ = (
#     Index('ix_users_email_address', 'email_address'),
#     Index('ix_users_username', 'username'),
# )
#will help with query performance and data integrity.

# Used lambda for the datetime defaults to ensure the timestamp is generated at record
# creation/update time rather than at class definition time.


