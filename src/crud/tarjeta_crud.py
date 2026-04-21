"""
CRUD para la entidad Tarjeta.
Gestiona tarjetas de transporte público asociadas a usuarios.
Incluye auditoría con usuario creador y editor.
"""

from typing import List, Optional
from uuid import UUID
from decimal import Decimal

from src.database.config import SessionLocal
from src.entities.tarjeta import Tarjeta


def crear(
    saldo: Decimal,
    id_usuario: UUID,
    id_usuario_creacion: UUID,
    tipo: Optional[str] = None,
    activo: bool = True,
) -> Tarjeta:
    """Crea una nueva tarjeta."""
    db = SessionLocal()
    try:
        tarjeta = Tarjeta(
            saldo=saldo,
            tipo=tipo.strip() if tipo else None,
            activo=activo,
            id_usuario=id_usuario,
            id_usuario_creacion=id_usuario_creacion,
        )
        db.add(tarjeta)
        db.commit()
        db.refresh(tarjeta)
        return tarjeta
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def obtener_por_id(id_tarjeta: UUID) -> Optional[Tarjeta]:
    """Obtiene una tarjeta por su ID."""
    db = SessionLocal()
    try:
        return db.query(Tarjeta).filter(Tarjeta.id_tarjeta == id_tarjeta).first()
    finally:
        db.close()


def obtener_todos() -> List[Tarjeta]:
    """Obtiene todas las tarjetas."""
    db = SessionLocal()
    try:
        return db.query(Tarjeta).all()
    finally:
        db.close()


def obtener_por_usuario(id_usuario: UUID) -> List[Tarjeta]:
    """Obtiene todas las tarjetas de un usuario."""
    db = SessionLocal()
    try:
        return db.query(Tarjeta).filter(Tarjeta.id_usuario == id_usuario).all()
    finally:
        db.close()


def obtener_activas() -> List[Tarjeta]:
    """Obtiene solo las tarjetas activas."""
    db = SessionLocal()
    try:
        return db.query(Tarjeta).filter(Tarjeta.activo == True).all()
    finally:
        db.close()


def actualizar(
    id_tarjeta: UUID,
    id_usuario_edita: UUID,
    *,
    saldo: Optional[Decimal] = None,
    tipo: Optional[str] = None,
    activo: Optional[bool] = None,
) -> Optional[Tarjeta]:
    """Actualiza una tarjeta existente."""
    db = SessionLocal()
    try:
        tarjeta = db.query(Tarjeta).filter(Tarjeta.id_tarjeta == id_tarjeta).first()
        if not tarjeta:
            return None
        if saldo is not None:
            tarjeta.saldo = saldo
        if tipo is not None:
            tarjeta.tipo = tipo.strip()
        if activo is not None:
            tarjeta.activo = activo
        tarjeta.id_usuario_edita = id_usuario_edita
        db.commit()
        db.refresh(tarjeta)
        return tarjeta
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def eliminar(id_tarjeta: UUID) -> bool:
    """Elimina una tarjeta."""
    db = SessionLocal()
    try:
        tarjeta = db.query(Tarjeta).filter(Tarjeta.id_tarjeta == id_tarjeta).first()
        if not tarjeta:
            return False
        db.delete(tarjeta)
        db.commit()
        return True
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
