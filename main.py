from fastapi import FastAPI
from database import Base, engine
from sqlalchemy.orm import Session
import models

# Reads all models that inherit from Base -> creates corresponding tables in database file if they don't exist yet
Base.metadata.create_all(bind=engine)

app = FastAPI()


def main():
    print("Hello from recipemanager!")


if __name__ == "__main__":
    main()
