from fastapi import APIRouter
from app.models import RegisterRequest
from app.database import create_api_key

router = APIRouter()

@router.post("/register")
def register_user(data: RegisterRequest):
    key = create_api_key(data.email)
    return {"api_key": key}
