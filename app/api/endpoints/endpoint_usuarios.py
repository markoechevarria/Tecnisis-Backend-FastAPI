from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.schema_usuario import UsuarioCreate, UsuarioUpdate, UsuarioResponse
from app.crud import crud_usuario as crud_usuario
from app.core.database import get_db

router = APIRouter()

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

@router.put("/actualizar/{id_usuario}", response_model=UsuarioResponse)
def actualizar_usuario(id_usuario: int, usuario_update: UsuarioUpdate, db: Session = Depends(get_db)):
    usuario = crud_usuario.actualizar_usuario(db, usuario_id=id_usuario, usuario_update=usuario_update)
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

@router.get("/evaluadoresArtisticos/", response_model=List[UsuarioResponse])
def obtener_evaluadores_artisticos( db: Session = Depends(get_db)):
    usuarios = crud_usuario.obtener_evaluadores_artisticos(db)
    if usuarios is None:
        raise HTTPException(status_code=404, detail="Evaluadores Artisticos no encontrados")
    return usuarios

@router.post("/registrarExperto/", response_model=UsuarioResponse)
def registrar_experto(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = crud_usuario.obtener_usuario_por_nombre(db, usuario_nombre=usuario.nombre)
    if db_usuario:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    return crud_usuario.registrar_experto(db=db, usuario=usuario)