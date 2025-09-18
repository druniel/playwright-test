import os
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Očekávaný klíč lze nastavit přes env var; pokud není, použije se default
EXPECTED_API_KEY = os.getenv("EXPECTED_API_KEY", "reqres-free-v1")

class Item(BaseModel):
    id: int
    name: str

@app.get("/users")
def get_users(x_api_key: Optional[str] = Header(None)):
    if x_api_key != EXPECTED_API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized - invalid x-api-key")
    # vrátíme demo data
    return {"page": 1, "data": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]}

@app.post("/items")
def create_item(item: Item, x_api_key: Optional[str] = Header(None)):
    if x_api_key != EXPECTED_API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized - invalid x-api-key")
    return {"status": "created", "item": item}