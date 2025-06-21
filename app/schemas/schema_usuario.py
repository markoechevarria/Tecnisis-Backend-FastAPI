from pydantic import BaseModel
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str
    correo: str
    contrasena: str
    id_perfil: int

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(UsuarioBase):
    nombre: Optional[str] = None 
    correo: Optional[str] = None 
    contrasena: Optional[str] = None 

class UsuarioResponse(UsuarioBase):
    id: int
    class Config:
        from_attributes = True