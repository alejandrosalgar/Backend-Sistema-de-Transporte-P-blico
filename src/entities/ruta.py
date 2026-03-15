"""
Entidad Ruta: línea o recorrido del sistema de transporte.
Incluye las 4 columnas de auditoría (creación/edición por usuario y fechas).
"""

import uuid

from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.database.config import Base


class Ruta(Base):
    """Modelo ORM Ruta."""

    __tablename__ = "ruta"

    id_ruta = Column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )
    codigo = Column(String(20), nullable=False)
    nombre = Column(String(150), nullable=True)
    activo = Column(Boolean, default=True)

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

    viajes = relationship("Viaje", back_populates="ruta")
