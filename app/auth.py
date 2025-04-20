from fastapi import Header, HTTPException
from app.database import is_valid_key

# Demo/testing keys
STATIC_API_KEYS = {
    "demo_user": "abc123xyz789secure",
    "test_client": "testkey-456-secure"
}

def validate_api_key(x_api_key: str = Header(...)):
    if x_api_key in STATIC_API_KEYS.values():
        return

    if is_valid_key(x_api_key):
        return

    raise HTTPException(status_code=401, detail="Unauthorized: Invalid API Key")
