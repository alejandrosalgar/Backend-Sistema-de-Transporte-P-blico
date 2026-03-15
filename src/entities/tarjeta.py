"""
Entidad Tarjeta: representa una tarjeta de transporte público.
Las demás entidades referencian a Usuario en id_usuario_crea e id_usuario_edita.
"""

import uuid
from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field
from sqlalchemy import Boolean, Column, DateTime, Float, String
from sqlalchemy import Numeric
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.database.config import Base


class Tarjeta(Base):
    """Modelo ORM Tarjeta."""

    __tablename__ = "tarjeta"

    id_tarjeta = Column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )
    saldo = Column(Numeric(10, 2), nullable=False)
    tipo = Column(String(20), nullable=True)
    activo = Column(Boolean, default=True)
    id_usuario = Column(
        PG_UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=False
    )
    id_usuario_creacion = Column(
        PG_UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=False
    )
    id_usuario_edita = Column(
        PG_UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=True
    )

    usuario_creacion = relationship("Usuario", foreign_keys=[id_usuario_creacion])
    usuario_edita = relationship("Usuario", foreign_keys=[id_usuario_edita])
    usuario = relationship("Usuario", foreign_keys=[id_usuario])

    fecha_creacion = Column(DateTime, server_default=func.now())
    fecha_edicion = Column(DateTime, server_default=func.now(), onupdate=func.now())
