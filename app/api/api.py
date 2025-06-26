from fastapi import APIRouter
from app.api.endpoints import endpoint_usuarios
from app.api.endpoints import endpoint_perfiles
from app.api.endpoints import endpoint_opciones

api_router = APIRouter()

api_router.include_router(endpoint_usuarios.router, prefix="/usuarios", tags=["usuarios"])
api_router.include_router(endpoint_perfiles.router, prefix="/perfil", tags=["perfiles"])
api_router.include_router(endpoint_opciones.router, prefix="/opciones", tags=["opciones"])