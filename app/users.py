from fastapi import APIRouter
from app.models import RegisterRequest
from app.database import create_api_key

from app.utils.helpers import create_temp_token
from app.models import RegisterRequest

router = APIRouter()

@router.post("/register")
def register_user(data: RegisterRequest):
    key = create_api_key(data.email)
    return {"api_key": key}



@router.post("/register/temp")
def register_temp_user(data: RegisterRequest):
    key = create_temp_token(data.email)
    return {"api_key": key}
