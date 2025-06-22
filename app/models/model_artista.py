from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.core.database import Base
from sqlalchemy.orm import sessionmaker, relationship

class Artista(Base):
    __tablename__ = "artistas"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    dni = Column(String)
    direccion = Column(String)
    telefono = Column(String)

    obra = relationship("Obra", back_populates="artista")
    solicitud = relationship("Solicitud", back_populates="artista")

    def __repr__(self):
        return f"<Artista(id={self.id}, name='{self.nombre}')>" 