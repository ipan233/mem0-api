from mem0 import Memory
from app.config import QDRANT_URL

_memory_cache = {}

def get_memory(collection: str):
    if collection not in _memory_cache:
        _memory_cache[collection] = Memory.from_config({
            "vector_store": {
                "provider": "qdrant",
                "config": {
                    "url": QDRANT_URL,
                    "collection_name": collection
                }
            }
        })
    return _memory_cache[collection]
