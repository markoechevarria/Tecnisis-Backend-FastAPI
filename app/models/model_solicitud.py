from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.core.database import Base
from sqlalchemy.orm import sessionmaker, relationship

class Solicitud(Base):
    __tablename__ = "solictitudes"

    id = Column(Integer, primary_key=True)
    id_artista = Column(Integer, ForeignKey("artistas.id"))
    id_obra = Column(Integer, ForeignKey("obras.id"))
    id_evaluador_artistico = Column(Integer, ForeignKey("usuarios.id"))
    aprobadaEvaluadorArtistico = Column(Boolean)
    aprobadaEValuadorEconomico = Column(Boolean)
    porcentaje_ganancia = Column(Integer)
    precio_venta = Column(Integer)

    artista = relationship("Artista", back_populates="solicitud")
    obra = relationship("Obra", back_populates="solicitud")
    usuario = relationship("Usuario", back_populates="solicitud")

    def __repr__(self):
        return f"<Solicitud(id={self.id}, name='{self.nombre}')>" 