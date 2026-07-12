import logging
from fastapi import APIRouter, HTTPException
from app.schemas.states import SignUpResponse, SignUpRequest
from app.database.db import SessionLocal
from app.services.auth_service import sign_up_user
from app.database.models.user import User
from pwdlib import PasswordHash

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/sign-up", response_model=SignUpResponse)
async def sign_up(req: SignUpRequest):
    db = SessionLocal()
    password_hash = PasswordHash.recommended()
    
    try:
        existing_user = (
            db.query(User).filter(User.email == req.email)
        ).first()
        
        if existing_user:
            raise HTTPException(
                status_code=409,
                detail="Email already exists."
            )
        
        hashed_password = password_hash.hash(req.password)
        
        user = sign_up_user(
            db=db,
            name=req.name,
            email=req.email,
            password=hashed_password
        )
        
        return {
            "message": "Account created successfully",
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error in sign up API: %s", e)
        raise HTTPException(
            status_code=500,
            detail="Could not create account"
        ) from e
    finally:
        db.close()
        