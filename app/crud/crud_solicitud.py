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

def evaluar_solicitud( id:int, aprobacion: int ,db: Session):
    solicitud =  db.query(Solicitud).filter(Solicitud.id == id).first()
    if (aprobacion == 1):
        solicitud.aprobadaEvaluadorArtistico = True
    elif (aprobacion == 0):
        solicitud.aprobadaEvaluadorArtistico = False
    db.commit()
    db.refresh(solicitud)
    return solicitud    

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

def asignar_precio_solicitud(db: Session, id: int, precio: int, porcentaje: int):
    solicitud = db.query(Solicitud).filter(Solicitud.id == id).first()
    if solicitud:
        solicitud.precio_venta = precio
        solicitud.porcentaje_ganancia = porcentaje
        solicitud.aprobadaEValuadorEconomico = True
        db.commit()
        db.refresh(solicitud)
        return solicitud
    return None     