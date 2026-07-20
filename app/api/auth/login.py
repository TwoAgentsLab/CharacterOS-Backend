import logging
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.schemas.states import SignInRequest, SignInResponse
from app.database.db import SessionLocal
from app.database.models.user import User
from app.services.auth_service import create_access_token
from pwdlib import PasswordHash

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/login", response_model=SignInResponse)
async def login(req: SignInRequest):
    db = SessionLocal()
    password_hash = PasswordHash.recommended()
    
    try:
        user = (
            db.query(User).filter(User.email == req.email)
        ).first()
        
        if not user.email:
            raise HTTPException(
                status_code=401,
                detail="Invalid Email Address"
            )
        
        if not password_hash.verify(
            req.password,
            user.hashed_password
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid Password"
            )
            
        token = create_access_token(user_id=user.id)
        
        response = JSONResponse(
            content={
                "message": "Login successfull",
                "user": {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email
                }
            }
        )
        
        response.set_cookie(
            key="access_token",
            value=token,
            httponly=True,
            secure=False,
            samesite="lax",
            max_age=3600
        )
        
        return response
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error in login up API: %s", e)
        raise HTTPException(
            status_code=500,
            detail="Could not login user"
        ) from e
    finally:
        db.close()
        