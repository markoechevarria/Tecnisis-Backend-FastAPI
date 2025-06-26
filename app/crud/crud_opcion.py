from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.model_opcion import Opcion
from app.schemas.schema_usuario import UsuarioCreate, UsuarioUpdate

def obtener_opciones(db: Session,  id_perfil: int ):
    return db.query(Opcion).filter(Opcion.id_perfil == id_perfil).all()