from pydantic import BaseModel
from typing import Optional

class TecnicaBase(BaseModel):
    nombre_tecnica: str
    nivel_apreciacion: str

class TecnicaCreate(TecnicaBase):
    pass

class TecnicaResponse(TecnicaBase):
    id: int
    class Config:
        from_attributes = True