from pydantic import BaseModel
from typing import Optional

class SolicitudBase(BaseModel):
    nombre: str
    id_artista: int
    id_obra: int
    id_evaluador_artistico: int
    aprobadaEvaluadorArtistico: bool
    aprobadaEValuadorEconomico: bool
    porcentaje_ganancia: float
    precio_venta: float

class SolicitudCreate(SolicitudBase):
    pass

class SolicitudResponse(SolicitudBase):
    id: int
    class Config:
        from_attributes = True