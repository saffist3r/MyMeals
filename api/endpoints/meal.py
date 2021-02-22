from typing import List

from fastapi import APIRouter, Depends, UploadFile
from starlette.requests import Request
from starlette.responses import PlainTextResponse, JSONResponse

from sqlalchemy.orm import Session
from db import crud, models, schemas
from db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
async def create_meal(meal: schemas.Meal, db: Session = Depends(get_db)):
    db_meal = models.Meal(image=meal.image, carbs=meal.carbs, time=meal.time)
    return crud.create_meal(db, db_meal)


@router.get("/", response_model=List[schemas.Meal])
async def get_meals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    meals = crud.get_meals(db, skip=skip, limit=limit)
    return meals


@router.get("/upload")
async def get_meals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    meals = crud.get_meals(db, skip=skip, limit=limit)
    return meals
