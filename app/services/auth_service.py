import logging
from app.database.models.user import User

logger = logging.getLogger(__name__)

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