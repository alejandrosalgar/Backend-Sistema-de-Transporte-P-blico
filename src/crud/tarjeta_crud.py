from typing import List, Optional
from uuid import UUID

from src.database.config import SessionLocal
from src.entities.tarjeta import Tarjeta

db = SessionLocal()
"""
id_tarjeta = Column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )
    saldo = Column(Float, nullable=False)
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
"""


def crear(
    saldo: float,
    id_usuario: UUID,
    id_usuario_creacion: UUID,
) -> Tarjeta:
    tarjeta = Tarjeta(
        saldo=saldo,
        id_usuario=id_usuario,
        id_usuario_creacion=id_usuario_creacion,
    )
    db.add(tarjeta)
    db.commit()
    db.refresh(tarjeta)
    return tarjeta


def obtener_por_id(id_tarjeta: UUID) -> Optional[Tarjeta]:
    return db.query(Tarjeta).filter(Tarjeta.id_tarjeta == id_tarjeta).first()


def obtener_todos() -> List[Tarjeta]:
    return db.query(Tarjeta).all()


def actualizar(
    id_tarjeta: UUID,
    id_usuario_edita: UUID,
    **kwargs: dict,
) -> Optional[Tarjeta]:
    tarjeta = obtener_por_id(id_tarjeta)
    if not tarjeta:
        return None
    for key, value in kwargs.items():
        if hasattr(tarjeta, key):
            setattr(tarjeta, key, value)
    tarjeta.id_usuario_edita = id_usuario_edita
    db.commit()
    db.refresh(tarjeta)
    return tarjeta


def eliminar(id_tarjeta: UUID) -> bool:
    tarjeta = obtener_por_id(id_tarjeta)
    if not tarjeta:
        return False
    db.delete(tarjeta)
    db.commit()
    return True
