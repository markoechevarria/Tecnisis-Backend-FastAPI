from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.model_tecnica import Tecnica
from app.schemas.schema_tecnica import TecnicaCreate

def obtener_tecnica_por_id(db: Session, id: int):
    return db.query(Tecnica).filter(Tecnica.id == id).first()

def registrar_tecnica(db: Session, tecnica: TecnicaCreate):
    db_tecnica = Tecnica(**tecnica.model_dump())
    db.add(db_tecnica)
    db.commit()
    db.refresh(db_tecnica)
    return db_tecnica