from app.schemas.states import NPCState
from app.database.db import SessionLocal
from app.database.models.npc import NPC

def load_npc_node(state: NPCState):
    db = SessionLocal()
    try:
        
        npc_id = state["npc_id"]
        
        npc = (
            db.query(NPC).filter(NPC.npc_code == npc_id)
        ).first()
        
        if npc is None:
            raise Exception("NPC not found in the database.")
        
        npc_data = {
            "id": npc.npc_code,
            "name": npc.name,
            "occupation": npc.occupation,
            "personality": npc.personality,
            "backstory": npc.backstory
        }
        
        return {
            "npc_data": npc_data
        }
    except Exception as e:
        print(f"Error in NPC node: {e}")
    finally:
        db.close()