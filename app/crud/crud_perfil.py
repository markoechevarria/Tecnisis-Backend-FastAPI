from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.model_usuario import Usuario
from app.models.model_perfil import Perfil
from app.schemas.schema_usuario import UsuarioCreate, UsuarioUpdate

def obtener_perfil_por_id_usuario(db: Session, perfil_id: int):
    return db.query(Perfil).filter(Perfil.id == perfil_id).first()

def obtener_perfil_id(db: Session, id: int):
    return db.query(Perfil).filter(Perfil.id == id).first()