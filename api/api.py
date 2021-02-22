from fastapi import APIRouter
from api.endpoints import meal

api_router = APIRouter()

api_router.include_router(meal.router, prefix="/meal", tags=["meal"])


@api_router.get("/")
async def root():
    return {"message": "MyMeals - API"}
