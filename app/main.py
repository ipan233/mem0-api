from fastapi import FastAPI, Depends
from app.schemas import AddMemoryReq, SearchMemoryReq
from app.security import verify_api_key
from app.memory import get_memory
from app.config import DEFAULT_COLLECTION

app = FastAPI(title="mem0 API", version="1.0.0")

@app.post("/memory/add", dependencies=[Depends(verify_api_key)])
def add_memory(req: AddMemoryReq):
    collection = req.collection or DEFAULT_COLLECTION
    memory = get_memory(collection)

    memory.add(
        req.content,
        user_id=req.user_id,
        metadata=req.metadata or {}
    )
    return {"status": "ok"}

@app.post("/memory/search", dependencies=[Depends(verify_api_key)])
def search_memory(req: SearchMemoryReq):
    collection = req.collection or DEFAULT_COLLECTION
    memory = get_memory(collection)

    results = memory.search(
        req.query,
        user_id=req.user_id,
        limit=req.limit
    )
    return results
