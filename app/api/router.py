from fastapi import APIRouter
from app.api.chat import chat
from app.api.auth import sign_up

api_router = APIRouter()

api_router.include_router(chat.router)
api_router.include_router(sign_up.router)