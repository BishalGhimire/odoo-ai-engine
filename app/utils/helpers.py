from datetime import datetime, timedelta
import secrets

# Temp tokens in memory (used for /register/temp)
temporary_tokens = {}

def create_temp_token(email: str) -> str:
    token = secrets.token_urlsafe(32)
    expires_at = datetime.utcnow() + timedelta(minutes=15)
    temporary_tokens[token] = {"email": email, "expires_at": expires_at}
    return token

def is_temp_token_valid(token: str) -> bool:
    token_data = temporary_tokens.get(token)
    return token_data and token_data["expires_at"] > datetime.utcnow()
