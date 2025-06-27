from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.schema_tecnica import TecnicaResponse
from app.crud import crud_tecnica
from app.core.database import get_db

router = APIRouter()

@router.get("/id/{id}", response_model=TecnicaResponse)
def obtener_tecnica_por_id(id: int, db: Session = Depends(get_db)):
    tecnica_db = crud_tecnica.obtener_tecnica_por_id(db, id=id)
    if tecnica_db is None:
        raise HTTPException(status_code=404, detail="Tecnica no encontrado")
    return tecnica_db