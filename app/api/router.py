from fastapi import APIRouter
from app.api.chat import chat
from app.api.auth import sign_up
from app.api.auth import login
from app.api.auth import me
from app.api.auth import logout

api_router = APIRouter()

api_router.include_router(chat.router)
api_router.include_router(sign_up.router)
api_router.include_router(login.router)
api_router.include_router(me.router)
api_router.include_router(logout.router)