from fastapi import APIRouter
from app.api.endpoints import usuarios

api_router = APIRouter()

api_router.include_router(usuarios.router, prefix="/usuarios", tags=["usuarios"])