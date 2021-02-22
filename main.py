from fastapi import FastAPI
from api.api import api_router

app = FastAPI(
    title="MyMeals - Backend",
    description="The backend for MyMeals",
    version="1.0.0",
)
app.include_router(api_router, prefix="/api")

