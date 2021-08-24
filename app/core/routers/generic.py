from fastapi import APIRouter
from app.core.models.pydantic.generic import ServerHealth
router = APIRouter()


@router.get("/", response_model=ServerHealth)
async def get():
    return ServerHealth(state="healthy")
