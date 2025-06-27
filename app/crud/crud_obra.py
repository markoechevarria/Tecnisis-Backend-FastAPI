from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.model_obra import Obra
from app.schemas.schema_obra import ObraCreate

def obtener_obra_por_id(db: Session, id: int):
    return db.query(Obra).filter(Obra.id == id).first()

def registrar_obra(db: Session, obra: ObraCreate):
    db_obra = Obra(**obra.model_dump())
    db.add(db_obra)
    db.commit()
    db.refresh(db_obra)
    return db_obra