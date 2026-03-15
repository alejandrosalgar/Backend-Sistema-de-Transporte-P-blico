"""
Entidad Viaje: un recorrido realizado por un vehículo en una ruta.
Incluye las 4 columnas de auditoría (creación/edición por usuario y fechas).
"""

import uuid

from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.database.config import Base


class Viaje(Base):
    """Modelo ORM Viaje."""

    __tablename__ = "viaje"

    id_viaje = Column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )
    id_ruta = Column(
        PG_UUID(as_uuid=True), ForeignKey("ruta.id_ruta"), nullable=False
    )
    id_vehiculo = Column(
        PG_UUID(as_uuid=True), ForeignKey("vehiculo.id_vehiculo"), nullable=False
    )
    id_estacion_origen = Column(
        PG_UUID(as_uuid=True), ForeignKey("estacion.id_estacion"), nullable=False
    )
    id_estacion_destino = Column(
        PG_UUID(as_uuid=True), ForeignKey("estacion.id_estacion"), nullable=False
    )
    fecha_hora_salida = Column(DateTime, nullable=False)

    id_usuario_creacion = Column(
        PG_UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=False
    )
    id_usuario_edita = Column(
        PG_UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=True
    )

    usuario_creacion = relationship("Usuario", foreign_keys=[id_usuario_creacion])
    usuario_edita = relationship("Usuario", foreign_keys=[id_usuario_edita])

    fecha_creacion = Column(DateTime, server_default=func.now())
    fecha_edicion = Column(DateTime, server_default=func.now(), onupdate=func.now())

    ruta = relationship("Ruta", back_populates="viajes")
    vehiculo = relationship("Vehiculo", back_populates="viajes")
    estacion_origen = relationship(
        "Estacion", foreign_keys=[id_estacion_origen], back_populates="viajes_origen"
    )
    estacion_destino = relationship(
        "Estacion", foreign_keys=[id_estacion_destino], back_populates="viajes_destino"
    )
