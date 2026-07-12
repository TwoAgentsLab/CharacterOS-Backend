from typing import TypedDict
from pydantic import BaseModel

class UserData(BaseModel):
    id: int
    name: int
    email: int

# Define the request model for the chat endpoint
class ChatRequest(BaseModel):
    npc_id: str
    player_id: str
    player_message: str
    
# Define the response model for the chat endpoint    z
class ChatResponse(BaseModel):
    npc_response: str
    
# Define the request model for the sign up endpoint
class SignUpRequest(BaseModel):
    name: str
    email: str
    password: str
    
# The Response from the database
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    
class SignUpResponse(BaseModel):
    message: str
    user: UserResponse

# Define the NPC state model
class NPCState(TypedDict):
    project_id: str
    npc_id: str
    player_id: str
    message: str
    npc_data: dict | None
    prompt: list | None
    response: str | None