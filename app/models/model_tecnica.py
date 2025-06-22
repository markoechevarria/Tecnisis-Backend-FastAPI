from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.core.database import Base
from sqlalchemy.orm import sessionmaker, relationship

class Tecnica(Base):
    __tablename__ = "tecnicas"

    id = Column(Integer, primary_key=True)
    nombre_tecnica = Column(String)
    nivel_apreciacion = Column(String)

    obra = relationship("Obra", back_populates="tecnica")

    def __repr__(self):
        return f"<Tecnica(id={self.id}, name='{self.nombre_tecnica}')>"