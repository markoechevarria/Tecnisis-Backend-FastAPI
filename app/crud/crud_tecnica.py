from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional

from app.models.model_tecnica import Tecnica
from app.models.model_obra import Obra
from app.schemas.schema_tecnica import TecnicaCreate, ObrasPorTecnica

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

def obtener_cantidad_obras_por_tecnica(db: Session):
    results = (
        db.query(
            Tecnica.id,
            Tecnica.nombre_tecnica,
            func.count(Tecnica.id).label("numero_obras")
        )
        .outerjoin(Obra)
        .group_by(Tecnica.id, Tecnica.nombre_tecnica)
        .all()
    )
    return [ ObrasPorTecnica(id=r.id, nombre_tecnica=r.nombre_tecnica, numero_obras=r.numero_obras) for r in results]