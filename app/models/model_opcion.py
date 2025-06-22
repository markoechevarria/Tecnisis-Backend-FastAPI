from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.core.database import Base
from sqlalchemy.orm import sessionmaker, relationship

class Opcion(Base):
    __tablename__ = "opciones"

    id = Column(Integer, primary_key=True)
    texto = Column(String)
    id_perfil = Column(Integer, ForeignKey("perfiles.id"))

    perfil = relationship("Perfil", back_populates="opcion")

    def __repr__(self):
        return f"<Opcion(id={self.id}, name='{self.nombre}')>"