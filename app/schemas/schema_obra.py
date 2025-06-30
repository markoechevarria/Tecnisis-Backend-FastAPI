from pydantic import BaseModel
from typing import Optional

class ObraBase(BaseModel):
    id_tecnica: int
    id_artista: int
    imagen_obra: str
    nombre: str
    fecha: str
    dimensiones: str

class ObraCreate(ObraBase):
    pass

class ObraResponse(ObraBase):
    id: int
    class Config:
        from_attributes = True