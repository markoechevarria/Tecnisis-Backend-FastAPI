from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.core.database import Base
from sqlalchemy.orm import sessionmaker, relationship

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    correo = Column(String, unique=True)
    contrasena = Column(String, nullable=True)
    id_perfil = Column(Integer, ForeignKey("perfiles.id"))

    perfil = relationship("Perfil", back_populates="usuario")

    def __repr__(self):
        return f"<Usuario(id={self.id}, name='{self.nombre}')>"