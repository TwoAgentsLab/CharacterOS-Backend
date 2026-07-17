import logging
from jose import jwt
from datetime import datetime, timedelta, UTC
from app.database.models.user import User
from app.config.config import SECRET_KEY

logger = logging.getLogger(__name__)

ALGORITHM = "HS256"

def sign_up_user(
    db,
    name: str,
    email: str,
    password: str
):  
    try:
        user = User(
            name=name,
            email=email,
            hashed_password=password
        )
        
        db.add(user)
        db.commit()
        db.refresh(user)
        
        return user
    except Exception:
        db.rollback()
        raise
    
def create_access_token(user_id: int):
    try:
        payload = {
            "sub": str(user_id),
            "exp": datetime.now(UTC) + timedelta(hours=1)
        }
        
        token = jwt.encode(
            payload,
            SECRET_KEY,
            algorithm=ALGORITHM
        )
        
        return token
    except Exception:
        raise