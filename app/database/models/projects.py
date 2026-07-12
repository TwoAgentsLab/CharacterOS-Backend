from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from app.database.db import Base

class Projects(Base):
    __tablename__ = "projects"
    
    id: Mapped[int] = mapped_column(
        primary_key=True
    )
    
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id")
    )
    
    name: Mapped[str] = mapped_column(String)
    api_key: Mapped[str] = mapped_column(
        String,
        unique=True
    )
    
    npcs = relationship(
        "NPC",
        back_populates="project"
    )
    
    user = relationship(
        "User",
        back_populates="projects"
    )