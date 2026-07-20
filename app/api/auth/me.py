import logging
from jose import jwt
from fastapi import APIRouter, HTTPException, Request
from app.config.config import SECRET_KEY
from app.database.models.user import User
from app.database.db import SessionLocal

logger = logging.getLogger(__name__)

router = APIRouter()
ALGORITHM = "HS256"

@router.get("/me")
async def me(req: Request):
    db = SessionLocal()
    token = req.cookies.get("access_token")
    
    if not token:
        raise HTTPException(
            status_code=401,
            detail="Not authenticated"
        )
        
    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )
    
    user_id = int(
        payload["sub"]
    )
    
    user = (
        db.query(User).filter(User.id == user_id)
    ).first()
    
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
        
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }