from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.schema_solicitud import SolicitudResponse, SolicitudCreate
from app.crud import crud_solicitud
from app.core.database import get_db

router = APIRouter()

@router.get("/", response_model=List[SolicitudResponse])
def obtener_solicitudes( db: Session = Depends(get_db)):
    solicitudes = crud_solicitud.obtener_solicitudes(db)
    return solicitudes

@router.get("/dni/", response_model=List[SolicitudResponse])
def obtener_solicitudes_dni(dni: str, db: Session = Depends(get_db)):
    solicitudes = crud_solicitud.obtener_solicitudes_dni(db)
    return solicitudes

@router.get("/id/{id}", response_model=SolicitudResponse)
def obtener_solicitud_por_id(id: str, db: Session = Depends(get_db)):
    solititud_db = crud_solicitud.obtener_solicitud_por_id(db, id=id)
    if solititud_db is None:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return 

@router.get("/artistico/{solicitudes_db_evaluador_artistico}", response_model=List[SolicitudResponse])
def obtener_solicitudes_por_id_evaluador_artistico(id_evaluador_artistico: int, db: Session = Depends(get_db)):
    solicitudes_db_evaluador_artistico = crud_solicitud.obtener_solicitudes_por_id_evaluador_artistico(db, id_evaluador_artistico= id_evaluador_artistico )
    return solicitudes_db_evaluador_artistico

@router.post("/registrarSolicitud", response_model=SolicitudResponse)
def registrar_solicitud(solicitud: SolicitudCreate, db: Session = Depends(get_db)):
    db_solicitud = crud_solicitud.registrar_solicitud(db=db, solicitud=solicitud)
    if db_solicitud is None:
        raise HTTPException(status_code=400, detail="Error al registrar la solicitud")
    return db_solicitud