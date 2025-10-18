import os
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# if not expected key, default will be used
EXPECTED_API_KEY = os.getenv("EXPECTED_API_KEY", "reqres-free-v1")

# how data should look like
class Item(BaseModel):
    id: int
    name: str

@app.get("/users")
def get_users(x_api_key: Optional[str] = Header(None)):
    if x_api_key != EXPECTED_API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized - invalid x-api-key")
    # returns expected data
    return {"page": 1, "data": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]}

@app.post("/items", status_code=201)
def create_item(item: Item, x_api_key: Optional[str] = Header(None)):
    if x_api_key != EXPECTED_API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized - invalid x-api-key")
    return {"status": "created", "item": item}