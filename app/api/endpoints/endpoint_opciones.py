from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.schema_opcion import OpcionResponse
from app.crud import crud_opcion as crud_opcion
from app.core.database import get_db

router = APIRouter()

@router.get("/{id_perfil}", response_model= List[OpcionResponse])
def obtener_opciones_por_id_perfil(  id_perfil: int, db: Session = Depends(get_db)):
    opciones = crud_opcion.obtener_opciones(db, id_perfil=id_perfil)
    return opciones