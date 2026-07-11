from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from app.database.db import Base

# Define the NPC model class that inherits from the Base class
class NPC(Base):
    __tablename__ = "npcs"
    
    id: Mapped[int] = mapped_column(
        primary_key=True
    )
    
    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id")
    )
    
    npc_code: Mapped[str] = mapped_column(
        String,
        unique=True
    )
    
    name: Mapped[str] = mapped_column(String)
    occupation: Mapped[str] = mapped_column(String)
    personality: Mapped[str] = mapped_column(String)
    backstory: Mapped[str] = mapped_column(String)
    
    project = relationship(
        "Projects",
        back_populates="npcs"
    )