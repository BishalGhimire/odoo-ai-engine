from fastapi import Header, HTTPException

VALID_API_KEYS = {
    "demo_client": "abc123xyz789secure"
}

def validate_api_key(x_api_key: str = Header(...)):
    if x_api_key not in VALID_API_KEYS.values():
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid API Key")