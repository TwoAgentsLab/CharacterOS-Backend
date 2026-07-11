from fastapi import APIRouter
from app.api.chat import chat

api_router = APIRouter()

api_router.include_router(chat.router)