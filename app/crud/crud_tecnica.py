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

def obtener_tecnicas(db: Session):
    return db.query(Tecnica).all()

def actualizar_tecnica(db: Session, id: int, tecnica: TecnicaCreate):
    db_tecnica = db.query(Tecnica).filter(Tecnica.id == id).first()
    if db_tecnica:
        for key, value in tecnica.model_dump().items():
            setattr(db_tecnica, key, value)
        db.commit()
        db.refresh(db_tecnica)
        return db_tecnica
    return None