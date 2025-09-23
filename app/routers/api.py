from fastapi import APIRouter, HTTPException
from app.models import ExampleRequest, ExampleResponse
from datetime import datetime
from typing import List

router = APIRouter()

# In-memory storage for demo (use database in production)
items_db = []
next_id = 1

@router.get("/items", response_model=List[ExampleResponse])
async def get_items():
    return items_db

@router.post("/items", response_model=ExampleResponse)
async def create_item(item: ExampleRequest):
    global next_id
    new_item = ExampleResponse(
        id=next_id,
        name=item.name,
        email=item.email,
        created_at=datetime.utcnow()
    )
    items_db.append(new_item)
    next_id += 1
    return new_item

@router.get("/items/{item_id}", response_model=ExampleResponse)
async def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")