"""
CRUD para la entidad Estación.
Gestiona paradas o estaciones del sistema de transporte.
"""

from typing import List, Optional
from uuid import UUID

from src.database.config import SessionLocal
from src.entities.estacion import Estacion


def crear(
    nombre: str,
    direccion: Optional[str] = None,
) -> Estacion:
    """Crea una nueva estación."""
    db = SessionLocal()
    try:
        estacion = Estacion(
            nombre=nombre.strip(),
            direccion=direccion.strip() if direccion else None,
        )
        db.add(estacion)
        db.commit()
        db.refresh(estacion)
        return estacion
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def obtener_por_id(id_estacion: UUID) -> Optional[Estacion]:
    """Obtiene una estación por su ID."""
    db = SessionLocal()
    try:
        return (
            db.query(Estacion).filter(Estacion.id_estacion == id_estacion).first()
        )
    finally:
        db.close()


def obtener_todos() -> List[Estacion]:
    """Obtiene todas las estaciones."""
    db = SessionLocal()
    try:
        return db.query(Estacion).all()
    finally:
        db.close()


def actualizar(
    id_estacion: UUID,
    *,
    nombre: Optional[str] = None,
    direccion: Optional[str] = None,
) -> Optional[Estacion]:
    """Actualiza una estación existente."""
    db = SessionLocal()
    try:
        estacion = (
            db.query(Estacion).filter(Estacion.id_estacion == id_estacion).first()
        )
        if not estacion:
            return None
        if nombre is not None:
            estacion.nombre = nombre.strip()
        if direccion is not None:
            estacion.direccion = direccion.strip()
        db.commit()
        db.refresh(estacion)
        return estacion
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def eliminar(id_estacion: UUID) -> bool:
    """Elimina una estación."""
    db = SessionLocal()
    try:
        estacion = (
            db.query(Estacion).filter(Estacion.id_estacion == id_estacion).first()
        )
        if not estacion:
            return False
        db.delete(estacion)
        db.commit()
        return True
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
