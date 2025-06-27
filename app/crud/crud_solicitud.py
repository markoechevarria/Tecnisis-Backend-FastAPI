from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.model_solicitud import Solicitud
from app.schemas.schema_solicitud import SolicitudCreate

def obtener_solicitud_por_id(db: Session, id: int):
    return db.query(Solicitud).filter(Solicitud.id == id).first()    

def obtener_solicitudes(db: Session):
    return db.query(Solicitud).all()

def obtener_solicitudes_dni(db: Session):
    return db.query(Solicitud).all()

def obtener_solicitudes_por_id_evaluador_artistico(db: Session, id_evaluador_artistico: int):
    return db.query(Solicitud).filter(Solicitud.id_evaluador_artistico == id_evaluador_artistico).all()

def obtener_solicitudes_aprobadasd_por_id_evaluador_artistico(db: Session, id_evaluador_artistico: int):
    return db.query(Solicitud).filter(Solicitud.id_evaluador_artistico == id_evaluador_artistico, Solicitud.aprobadaEvaluadorArtistico == True).all()

def registrar_solicitud(db: Session, solicitud: SolicitudCreate):
    db_solicitud = Solicitud(**solicitud.model_dump())
    db.add(db_solicitud)
    db.commit()
    db.refresh(db_solicitud)
    return db_solicitud