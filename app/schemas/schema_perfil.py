from pydantic import BaseModel
from typing import Optional

class PerfilBase(BaseModel):
    nombre: str

class PerfilResponse(PerfilBase):
    id: int
    class Config:
        from_attributes = True