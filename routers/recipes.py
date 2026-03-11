from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models import Recipe
from schemas import RecipeCreate, RecipeUpdate, RecipeResponse
from typing import List, Optional


router = APIRouter(
    prefix="/recipes",
    tags=["recipes"]
)


# Create
# POST /recipes/
@router.post("/", response_model=RecipeResponse, status_code=status.HTTP_201_CREATED)
def create_recipe(recipe: RecipeCreate, db: Session = Depends(get_db)):
    # Create new SQLAlchemy model instance from incoming schema
    db_recipe = Recipe(**recipe.model_dump())

    db.add(db_recipe)   # Stage new recipe to be saved
    db.commit()     # Write to database file
    db.refresh(db_recipe)   # Reload it so db_recipe now includes id and created_at

    return db_recipe


# Read All - returns list of all recipes
# GET /recipes/
@router.get("/", response_model=List[RecipeResponse])
def get_recipes(category: Optional[str] = None, db: Session = Depends(get_db)):

    query = db.query(Recipe)

    # if a category was passed in the URL add a WHERE clause to query
    if category:
        query = query.filter(Recipe.category == category)
    return query.all()


# Read One - returns a single recipe by its ID, raises 404 if ID does not exist
# GET /recipes/{id}
@router.get("/{recipe_id}", response_model=RecipeResponse)
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):

    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if db_recipe is None:
       raise HTTPException(
           status_code=status.HTTP_404_NOT_FOUND,
           detail=f"Recipe with id {recipe_id} not found"
       )
    return db_recipe


# Update - updates only the fields that were actually sent in, fields not included left unchanged
# PUT /recipes/{id}
@router.put("/{recipe_id}", response_model=RecipeResponse)
def update_recipe(recipe_id: int, recipe: RecipeUpdate, db: Session = Depends(get_db)):

    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()

    if db_recipe is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= f"Recipe with id {recipe_id} not found"
        )
    update_data = recipe.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_recipe, field, value)

    db.commit()
    db.refresh(db_recipe)

    return db_recipe


# Delete - delete recipe by ID, returns 204 No Content response on success
# DELETE /recipes/{id}
@router.delete("/{recipe_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):

    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()

    if db_recipe is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Recipe with id {recipe_id} not found"
        )

    db.delete(db_recipe)
    db.commit()
