from sqlalchemy.orm import Session

from . import models, schemas


# Meals Related CRUD

# Read

def get_meals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Meal).offset(skip).limit(limit).all()


# Create

def create_meal(db: Session, meal: schemas.Meal):
    db_meal = models.Meal(id='', image=meal.image, carbs=meal.carbs, time=meal.time)
    db.add(db_meal)
    db.commit()
    db.refresh(db_meal)
    return db_meal
