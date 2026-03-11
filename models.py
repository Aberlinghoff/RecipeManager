from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    #Integer primary key
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True)
    ingredients = Column(Text, nullable=False)
    instructions = Column(Text, nullable=False)
    category = Column(String, nullable=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())