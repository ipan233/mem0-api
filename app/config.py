import os
from dotenv import load_dotenv

load_dotenv()

MEM0_API_KEY = os.getenv("MEM0_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
DEFAULT_COLLECTION = os.getenv("DEFAULT_COLLECTION", "mem0_default")
