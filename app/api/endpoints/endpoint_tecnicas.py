from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.schema_tecnica import TecnicaResponse, TecnicaCreate
from app.crud import crud_tecnica
from app.core.database import get_db

router = APIRouter()

@router.get("/id/{id}", response_model=TecnicaResponse)
def obtener_tecnica_por_id(id: int, db: Session = Depends(get_db)):
    tecnica_db = crud_tecnica.obtener_tecnica_por_id(db, id=id)
    if tecnica_db is None:
        raise HTTPException(status_code=404, detail="Tecnica no encontrado")
    return tecnica_db

@router.post("/registrarTecnica/", response_model=TecnicaResponse)
def registrar_experto(tecnica: TecnicaCreate, db: Session = Depends(get_db)):
    db_tecnica = crud_tecnica.registrar_tecnica(db, tecnica=tecnica)
    if db_tecnica is None:
        raise HTTPException(status_code=400, detail="Error al registrar la técnica")
    return db_tecnica