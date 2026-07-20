from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/logout")
async def logout():
    response = JSONResponse(
        content={
            "message": "Logged out successfully"
        }
    )
    
    response.delete_cookie(
        key="access_token",
        httponly=True,
        samesite="lax"
    )
    
    return response