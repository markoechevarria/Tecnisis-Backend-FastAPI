from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.schema_obra import ObraResponse, ObraCreate
from app.crud import crud_obra
from app.core.database import get_db

router = APIRouter()

@router.get("/id/{id}", response_model=ObraResponse)
def obtener_obra_por_id(id: int, db: Session = Depends(get_db)):
    obra_db = crud_obra.obtener_obra_por_id(db, id=id)
    if obra_db is None:
        raise HTTPException(status_code=404, detail="Obra no encontrado")
    return obra_db

@router.post("/registrar/", response_model=ObraResponse, status_code=status.HTTP_201_CREATED)
def registrar_obra(obra: ObraCreate, db: Session = Depends(get_db)):
    db_obra = crud_obra.registrar_obra(db=db, obra=obra)
    if db_obra is None:
        raise HTTPException(status_code=400, detail="Error al registrar la obra")
    return db_obra