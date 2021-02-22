from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base


class Meal(Base):
    __tablename__ = "meal"
    id = Column(Integer, primary_key=True, index=True)
    image = Column(String)
    carbs = Column(Float)
    time = Column(String)
