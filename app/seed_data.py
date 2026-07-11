from app.database.db import SessionLocal
from app.database.models.npc import NPC
from app.database.models.projects import Projects

db = SessionLocal()

project = Projects(
    name="OAK Village",
    api_key="8aDcslYZUx1uuTeKgCWLZAsmw7chOFua"
)

project.npcs = [
    NPC(
        npc_code = "merchant_01",
        name="Thomas",
        occupation = "Merchant",
        personality = "Friendly and lovely",
        backstory = "Lives in OAK Village"
    ),
    NPC(
        npc_code = "guard_01",
        name="Max",
        occupation = "Castle Main Gate Guard",
        personality = "Rude",
        backstory = "Distrust Strangers"
    )
]

db.add(project)
db.commit()