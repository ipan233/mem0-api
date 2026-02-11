from pydantic import BaseModel
from typing import Optional, Dict

class AddMemoryReq(BaseModel):
    user_id: str
    content: str
    metadata: Optional[Dict] = None
    collection: Optional[str] = None

class SearchMemoryReq(BaseModel):
    user_id: str
    query: str
    limit: int = 5
    collection: Optional[str] = None
