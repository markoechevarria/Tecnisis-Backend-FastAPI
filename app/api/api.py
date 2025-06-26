from fastapi import APIRouter
from app.api.endpoints import endpoint_usuarios
from app.api.endpoints import endpoint_perfiles
from app.api.endpoints import endpoint_opciones
from app.api.endpoints import endpoint_artistas
from app.api.endpoints import endpoint_obras
from app.api.endpoints import endpoint_tecnicas
from app.api.endpoints import endpoint_solicitudes

api_router = APIRouter()

api_router.include_router(endpoint_usuarios.router, prefix="/usuarios", tags=["usuarios"])
api_router.include_router(endpoint_perfiles.router, prefix="/perfil", tags=["perfiles"])
api_router.include_router(endpoint_opciones.router, prefix="/opciones", tags=["opciones"])
api_router.include_router(endpoint_artistas.router, prefix="/artistas", tags=["artistas"])
api_router.include_router(endpoint_obras.router, prefix="/obras", tags=["obras"])
api_router.include_router(endpoint_tecnicas.router, prefix="/tecnicas", tags=["tecnicas"])
api_router.include_router(endpoint_solicitudes.router, prefix="/solicitudes", tags=["solicitudes"])