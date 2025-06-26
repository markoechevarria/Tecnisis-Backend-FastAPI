from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.schema_artista import ArtistaCreate, ArtistaResponse
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

"""

@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def crear_nuevo_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = crud_usuario.obtener_usuario_por_nombre(db, usuario_nombre=usuario.nombre )
    if db_usuario: 
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    return crud_usuario.create_usuario(db=db, usuario=usuario)

@router.get("/", response_model= List[UsuarioResponse])
def obtener_usuarios( db: Session = Depends(get_db) ):
    usuarios = crud_usuario.obtener_usuarios(db)
    return usuarios

@router.get("/{usuario_id}", response_model=UsuarioResponse)
def obtener_usuario_por_id(usuario_id: int, db: Session = Depends(get_db)):
    usuario = crud_usuario.obtener_usuario_por_id(db, usuario_id = usuario_id)
    if usuario is None: 
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.put("/{usuario_id}", response_model=UsuarioResponse)
def actualizar_usuario(usuario_id: int, usuario_update: UsuarioUpdate, db: Session = Depends(get_db)):
    usuario = crud_usuario.actualizar_usuario(db, usuario_id=usuario_id, usuario_update=usuario_update)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.delete("/{id_usuario}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    success = crud_usuario.eliminar_usuario(db, usuario_id=usuario_id)
    if not success: 
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return { "message": "Usuario eliminado exitosamente"}

@router.get("/ingresar/", response_model=UsuarioResponse)
def ingresar_usuario(correo: str, contrasena: str, db: Session = Depends(get_db)):
    usuario = crud_usuario.ingresar_usuario(db, correo=correo, contrasena=contrasena)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado, registrese primero")
    return usuario

"""