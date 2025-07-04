from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.schema_artista import ArtistaCreate, ArtistaResponse, ArtistaPrecios
from app.crud import crud_artista as crud_artista
from app.core.database import get_db

router = APIRouter()

@router.get("/{dni}", response_model=ArtistaResponse)
def obtener_artista_por_dni(dni: str, db: Session = Depends(get_db)):
    artista = crud_artista.obtener_artista_por_dni(db, dni=dni)
    if artista is None:
        raise HTTPException(status_code=404, detail="Artista no encontrado")
    return artista

@router.get("/id/{id}", response_model=ArtistaResponse)
def obtener_artista_por_id(id: int, db: Session = Depends(get_db)):
    artista = crud_artista.obtener_artista_por_id(db, id=id)
    if artista is None:
        raise HTTPException(status_code=404, detail="Artista no encontrado")
    return artista

@router.post("/", response_model=ArtistaResponse, status_code=status.HTTP_201_CREATED)
def crear_nuevo_artista(artista: ArtistaCreate, db: Session = Depends(get_db)):
    db_artista = crud_artista.obtener_artista_por_dni(db, dni=artista.dni )
    if db_artista: 
        raise HTTPException(status_code=400, detail="El artista ya existe")
    return crud_artista.crear_artista(db=db, artista=artista)

@router.get("/precios/", response_model=List[ArtistaPrecios])
def obtener_precio_promedio_solicitudes_por_artista(db: Session = Depends(get_db)):
    precios = crud_artista.obtener_precio_promedio_solicitudes_por_artista(db)
    if not precios:
        raise HTTPException(status_code=404, detail="No se encontraron precios")
    return precios