from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base
from sqlalchemy.orm import sessionmaker, relationship

class Perfil(Base):
    __tablename__ = "perfiles"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)

    usuario = relationship("Usuario", back_populates="perfil")

    def __repr__(self):
        return f"<Usuario(id={self.id}, perfil='{self.nombre}')>"