"""
Entidad Vehículo: unidad de transporte (bus, etc.).
Sin columnas de auditoría.
"""

import uuid

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import relationship

from src.database.config import Base


class Vehiculo(Base):
    """Modelo ORM Vehículo."""

    __tablename__ = "vehiculo"

    id_vehiculo = Column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )
    placa = Column(String(20), nullable=False)
    modelo = Column(String(100), nullable=True)
    capacidad = Column(Integer, nullable=True)

    viajes = relationship("Viaje", back_populates="vehiculo")
