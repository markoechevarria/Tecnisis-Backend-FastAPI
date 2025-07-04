from pydantic import BaseModel
from typing import Optional

class ArtistaBase(BaseModel):
    nombre: str
    dni: str
    direccion: str
    telefono: str

class ArtistaCreate(ArtistaBase):
    pass

class ArtistaUpdate(ArtistaBase):
    nombre: Optional[str] = None
    dni: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None

class ArtistaResponse(ArtistaBase):
    id: int
    class Config:
        from_attributes = True

class ArtistaPrecios(BaseModel):
    nombre: str
    precio: int

    class Config:
        from_attributes = True