from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from app.services.progress_service import ProgressService
from app.models.progress import Progress
from datetime import date

router = APIRouter()

progress_service = ProgressService()

class ProgressIn(BaseModel):
    user_id: int
    activity: str
    duration: int
    distance: float
    intensity: int
    calories_burned: float
    date: date

@router.post("/progress", response_model=Progress)
def create_progress(progress_in: ProgressIn):
    return progress_service.create_progress(progress_in)

@router.get("/progress/{user_id}", response_model=List[Progress])
def get_user_progress(user_id: int):
    return progress_service.get_user_progress(user_id)
