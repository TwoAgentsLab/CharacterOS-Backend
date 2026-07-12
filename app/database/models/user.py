from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, func
from app.database.db import Base
from datetime import datetime, timezone

class User(Base):
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(
        primary_key=True
    )
    
    name: Mapped[str] = mapped_column(String)
    email: Mapped[int] = mapped_column(String, unique=True)
    hashed_password: Mapped[int] = mapped_column(String)
    
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    
    projects = relationship(
        "Projects",
        back_populates="user"
    )