from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    correo = Column(String, index=True, unique=True)
    contrasena = Column(String, nullable=True)

    def __repr__(self):
        return f"<Usuario(id={self.id}, name='{self.nombre}')>"