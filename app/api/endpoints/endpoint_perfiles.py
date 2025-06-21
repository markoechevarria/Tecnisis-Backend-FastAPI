from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.schema_perfil import PerfilResponse
from app.schemas.schema_usuario import UsuarioCreate, UsuarioUpdate, UsuarioResponse
from app.crud import crud_usuario
from app.crud import crud_perfil
from app.core.database import get_db

router = APIRouter()

@router.get("/{id_usuario}", response_model=PerfilResponse)
def obtener_perfil_usuario( id_usuario: int, db: Session = Depends(get_db) ):
    usuario = crud_usuario.obtener_usuario_por_id(db, usuario_id= id_usuario)
    perfil = crud_perfil.obtener_perfil_por_id_usuario(db, usuario.id_perfil)
    if perfil is None: 
        raise HTTPException(status_code=404, detail="Perfil no encontrado")
    return perfil