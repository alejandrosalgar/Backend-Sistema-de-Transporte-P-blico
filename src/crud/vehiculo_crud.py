"""
CRUD para la entidad Vehículo.
Gestiona unidades de transporte (buses, etc.).
"""

from typing import List, Optional
from uuid import UUID

from src.database.config import SessionLocal
from src.entities.vehiculo import Vehiculo


def crear(
    placa: str,
    modelo: Optional[str] = None,
    capacidad: Optional[int] = None,
) -> Vehiculo:
    """Crea un nuevo vehículo."""
    db = SessionLocal()
    try:
        vehiculo = Vehiculo(
            placa=placa.strip(),
            modelo=modelo.strip() if modelo else None,
            capacidad=capacidad,
        )
        db.add(vehiculo)
        db.commit()
        db.refresh(vehiculo)
        return vehiculo
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def obtener_por_id(id_vehiculo: UUID) -> Optional[Vehiculo]:
    """Obtiene un vehículo por su ID."""
    db = SessionLocal()
    try:
        return (
            db.query(Vehiculo).filter(Vehiculo.id_vehiculo == id_vehiculo).first()
        )
    finally:
        db.close()


def obtener_por_placa(placa: str) -> Optional[Vehiculo]:
    """Obtiene un vehículo por su placa."""
    db = SessionLocal()
    try:
        return db.query(Vehiculo).filter(Vehiculo.placa == placa.strip()).first()
    finally:
        db.close()


def obtener_todos() -> List[Vehiculo]:
    """Obtiene todos los vehículos."""
    db = SessionLocal()
    try:
        return db.query(Vehiculo).all()
    finally:
        db.close()


def actualizar(
    id_vehiculo: UUID,
    *,
    placa: Optional[str] = None,
    modelo: Optional[str] = None,
    capacidad: Optional[int] = None,
) -> Optional[Vehiculo]:
    """Actualiza un vehículo existente."""
    db = SessionLocal()
    try:
        vehiculo = (
            db.query(Vehiculo).filter(Vehiculo.id_vehiculo == id_vehiculo).first()
        )
        if not vehiculo:
            return None
        if placa is not None:
            vehiculo.placa = placa.strip()
        if modelo is not None:
            vehiculo.modelo = modelo.strip()
        if capacidad is not None:
            vehiculo.capacidad = capacidad
        db.commit()
        db.refresh(vehiculo)
        return vehiculo
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def eliminar(id_vehiculo: UUID) -> bool:
    """Elimina un vehículo."""
    db = SessionLocal()
    try:
        vehiculo = (
            db.query(Vehiculo).filter(Vehiculo.id_vehiculo == id_vehiculo).first()
        )
        if not vehiculo:
            return False
        db.delete(vehiculo)
        db.commit()
        return True
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
