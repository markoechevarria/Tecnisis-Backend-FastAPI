from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.model_usuario import Usuario
from app.models.model_perfil import Perfil
from app.schemas.schema_usuario import UsuarioCreate, UsuarioUpdate

def crear_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = Usuario(**usuario.model_dump())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def obtener_usuario_por_id(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def obtener_usuario_por_nombre(db: Session, usuario_nombre: str):
    return db.query(Usuario).filter(Usuario.nombre == usuario_nombre).first()

def obtener_usuarios(db: Session ):
    return db.query(Usuario).all()

def actualizar_usuario(db: Session, usuario_id: int, usuario_update: UsuarioUpdate):
    db_usuario = db.query(Usuario).filter( Usuario.id == usuario_id).first()
    if db_usuario:
        for key, value in usuario_update.model_dump(exclude_unset=True).items():
            setattr(db_usuario, key, value)
        db.add(db_usuario)
        db.commit()
        db.refresh(db_usuario)
    return db_usuario

def eliminar_usuario(db: Session, usuario_id: int):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
        return True
    return False

def obtener_perfil_usuario(db: Session, usuario_id: int):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    perfil = db.query(Perfil).filter(Perfil.id == usuario.id).first()
    return perfil

def ingresar_usuario(db: Session, correo: str, contrasena: str):
    return db.query(Usuario).filter(Usuario.correo == correo, Usuario.contrasena == contrasena).first()

def obtener_evaluadores_artisticos(db: Session ):
    return db.query(Usuario).filter(Usuario.id_perfil == 2 ).all()