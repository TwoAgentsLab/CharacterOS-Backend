from app.database.db import engine, Base
from app.database.models.npc import NPC
from app.database.models.projects import Projects

Base.metadata.create_all(bind=engine)