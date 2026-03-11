from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Input Schema, will automatically reject any request that doesn't match this shape

class RecipeCreate(BaseModel):
    title: str
    description: Optional[str] = None
    ingredients: str
    instructions: str
    category: Optional[str] = None

# Update Schema, every field is optional so individual fields may be updated without updating the whole recipe

class RecipeUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    ingredients: Optional[str] = None
    instructions: Optional[str] = None
    category: Optional[str] = None


# Response Schema, includes fields from RecipeCreate plus database generated fields (id and created_at)

class RecipeResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    ingredients: str
    instructions: str
    category: Optional[str] = None
    created_at: datetime
    
    class Config:
        from_attributes = True