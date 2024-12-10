from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, Boolean, ForeignKey, DateTime
from uuid import uuid4
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, UTC, date
from typing import List, Optional
from .base import Base


class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(String(1000), nullable=False)
    is_public: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        nullable=False
    )

    # Relationship to User
    user = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"<Post {self.title}>"