from app.database.db import engine, Base
from app.database.models.npc import NPC
from app.database.models.projects import Projects
from app.database.models.user import User

Base.metadata.create_all(bind=engine)