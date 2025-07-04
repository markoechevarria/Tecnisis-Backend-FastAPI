from sqlalchemy.orm import Session
from decimal import Decimal
from sqlalchemy import func
from typing import List, Optional

from app.models.model_artista import Artista
from app.models.model_solicitud import Solicitud
from app.models.model_perfil import Perfil
from app.schemas.schema_artista import ArtistaCreate, ArtistaPrecios

def obtener_artista_por_dni(db: Session, dni: str):
    return db.query(Artista).filter(Artista.dni == dni).first()    

def obtener_artista_por_id(db: Session, id: int):
    return db.query(Artista).filter(Artista.id == id).first()

def crear_artista(db: Session, artista: ArtistaCreate):
    db_artista = Artista(**artista.model_dump())
    db.add(db_artista)
    db.commit()
    db.refresh(db_artista)
    return db_artista

def obtener_precio_promedio_solicitudes_por_artista(db: Session):
    results = (
        db.query(
            Artista.id,
            Artista.nombre,
            func.avg(Solicitud.precio_venta).label("precio_promedio")
        )
        .outerjoin(Solicitud, Artista.id == Solicitud.id_artista)
        .group_by(Artista.id, Artista.nombre)
        .all()
    )

    return [
        ArtistaPrecios(
            nombre=r.nombre,
            precio=int(r.precio_promedio) if r.precio_promedio is not None else 0
        ) for r in results
    ]