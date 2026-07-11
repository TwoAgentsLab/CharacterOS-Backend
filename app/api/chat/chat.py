import logging
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.schemas.states import ChatRequest
from app.graph.npc_graph import build_graph
from app.database.db import SessionLocal
from app.database.models.projects import Projects
    
logger = logging.getLogger(__name__)

# Define the API router and request model for chat functionality
router = APIRouter()
graph = build_graph()
security = HTTPBearer()
    
@router.post("/chat")
async def chat(req: ChatRequest, creds: HTTPAuthorizationCredentials = Depends(security)):
    db = SessionLocal()
    
    try:
        api_key = creds.credentials
        print("API KEY: ",api_key)
        key = api_key.replace(
            "Bearer ",
            ""
        )
        
        project = (
            db.query(Projects).filter(Projects.api_key == key)
        ).first()
        
        if project is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid API Key"
            )
        
        state = {
            "project_id": project.id,
            "npc_id": req.npc_id,
            "player_id": req.player_id,
            "message": req.player_message
        }
        
        result = graph.invoke(state)
        
        return {
            "response": result["response"]
        }
    except Exception as e:
        logger.error("Error from test API: %s", e)
    finally:
        db.close()