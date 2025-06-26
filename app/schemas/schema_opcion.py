from pydantic import BaseModel
from typing import Optional

class OpcionBase(BaseModel):
    id: int
    texto: str
    id_perfil: int

class OpcionResponse(OpcionBase):
    id: int
    class Config:
        from_attributes = True