import shutil


from typing import List
from datetime import datetime

import config

from fastapi import APIRouter, Depends, UploadFile

from sqlalchemy.orm import Session
from db import crud, models, schemas
from db.database import SessionLocal, engine

from fastapi import FastAPI, File, UploadFile

import os.path

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
    db_meal = models.Meal(image=meal.image, carbs=meal.carbs, time=datetime.now())
    crud.create_meal(db, db_meal)
    return "Success"


@router.get("/", response_model=List[schemas.Meal])
async def get_meals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    meals = crud.get_meals(db, skip=skip, limit=limit)
    return meals


@router.put("/upload/")
async def upload_image(file: UploadFile = File(...)):
    file_to_save = config.IMAGES_DIRECTORY + file.filename + str(datetime.timestamp(datetime.now())) + ".png"
    with open(file_to_save, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file_to_save}
