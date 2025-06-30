from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.core.database import Base
from sqlalchemy.orm import sessionmaker, relationship

class Obra(Base):
    __tablename__ = "obras"

    id = Column(Integer, primary_key=True)
    id_tecnica = Column(Integer, ForeignKey("tecnicas.id"))
    id_artista = Column(Integer, ForeignKey("artistas.id"))
    imagen_obra = Column(String)
    nombre = Column(String, nullable=False)
    fecha = Column(String)
    dimensiones = Column(String)

    tecnica = relationship("Tecnica", back_populates="obra")
    artista = relationship("Artista", back_populates="obra")
    solicitud = relationship("Solicitud", back_populates="obra")

    def __repr__(self):
        return f"<Obra(id={self.id}')>" 