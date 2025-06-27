from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.model_artista import Artista
from app.models.model_perfil import Perfil
from app.schemas.schema_artista import ArtistaCreate, ArtistaUpdate

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