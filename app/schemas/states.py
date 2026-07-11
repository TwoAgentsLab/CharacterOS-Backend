from typing import TypedDict
from pydantic import BaseModel

# Define the request model for the chat endpoint
class ChatRequest(BaseModel):
    npc_id: str
    player_id: str
    player_message: str
    
# Define the response model for the chat endpoint    
class ChatResponse(BaseModel):
    npc_id: str
    npc_response: str

# Define the NPC state model
class NPCState(TypedDict):
    project_id: str
    npc_id: str
    player_id: str
    message: str
    npc_data: dict | None
    prompt: list | None
    response: str | None