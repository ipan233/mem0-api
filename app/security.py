from fastapi import Header, HTTPException
from app.config import MEM0_API_KEY

def verify_api_key(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid auth header")

    token = authorization.split(" ", 1)[1]
    if token != MEM0_API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")
