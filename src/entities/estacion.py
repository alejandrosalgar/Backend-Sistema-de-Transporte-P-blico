"""
Entidad Estación: parada o estación del sistema de transporte.
Sin columnas de auditoría.
"""

import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import relationship

from src.database.config import Base


class Estacion(Base):
    """Modelo ORM Estación."""

    __tablename__ = "estacion"

    id_estacion = Column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )
    nombre = Column(String(150), nullable=False)
    direccion = Column(String(255), nullable=True)

    viajes_origen = relationship(
        "Viaje",
        foreign_keys="Viaje.id_estacion_origen",
        back_populates="estacion_origen",
    )
    viajes_destino = relationship(
        "Viaje",
        foreign_keys="Viaje.id_estacion_destino",
        back_populates="estacion_destino",
    )
