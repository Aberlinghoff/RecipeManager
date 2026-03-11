from fastapi import FastAPI
from database import Base, engine
import models
from routers import recipes

# Reads all models that inherit from Base -> creates corresponding tables in database file if they don't exist yet
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Recipe Manager API")

app.include_router(recipes.router)


