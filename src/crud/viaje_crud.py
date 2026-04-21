"""
CRUD para la entidad Viaje.
Gestiona los recorridos realizados por vehículos en rutas.
Incluye auditoría con usuario creador y editor.
"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from src.database.config import SessionLocal
from src.entities.viaje import Viaje


def crear(
    id_ruta: UUID,
    id_vehiculo: UUID,
    id_estacion_origen: UUID,
    id_estacion_destino: UUID,
    fecha_hora_salida: datetime,
    id_usuario_creacion: UUID,
) -> Viaje:
    """Crea un nuevo viaje."""
    db = SessionLocal()
    try:
        viaje = Viaje(
            id_ruta=id_ruta,
            id_vehiculo=id_vehiculo,
            id_estacion_origen=id_estacion_origen,
            id_estacion_destino=id_estacion_destino,
            fecha_hora_salida=fecha_hora_salida,
            id_usuario_creacion=id_usuario_creacion,
        )
        db.add(viaje)
        db.commit()
        db.refresh(viaje)
        return viaje
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def obtener_por_id(id_viaje: UUID) -> Optional[Viaje]:
    """Obtiene un viaje por su ID."""
    db = SessionLocal()
    try:
        return db.query(Viaje).filter(Viaje.id_viaje == id_viaje).first()
    finally:
        db.close()


def obtener_todos() -> List[Viaje]:
    """Obtiene todos los viajes."""
    db = SessionLocal()
    try:
        return db.query(Viaje).all()
    finally:
        db.close()


def obtener_por_ruta(id_ruta: UUID) -> List[Viaje]:
    """Obtiene todos los viajes de una ruta."""
    db = SessionLocal()
    try:
        return db.query(Viaje).filter(Viaje.id_ruta == id_ruta).all()
    finally:
        db.close()


def obtener_por_vehiculo(id_vehiculo: UUID) -> List[Viaje]:
    """Obtiene todos los viajes de un vehículo."""
    db = SessionLocal()
    try:
        return db.query(Viaje).filter(Viaje.id_vehiculo == id_vehiculo).all()
    finally:
        db.close()


def obtener_por_estacion_origen(id_estacion: UUID) -> List[Viaje]:
    """Obtiene todos los viajes que salen de una estación."""
    db = SessionLocal()
    try:
        return (
            db.query(Viaje).filter(Viaje.id_estacion_origen == id_estacion).all()
        )
    finally:
        db.close()


def obtener_por_estacion_destino(id_estacion: UUID) -> List[Viaje]:
    """Obtiene todos los viajes que llegan a una estación."""
    db = SessionLocal()
    try:
        return (
            db.query(Viaje).filter(Viaje.id_estacion_destino == id_estacion).all()
        )
    finally:
        db.close()


def obtener_por_fecha(fecha: datetime) -> List[Viaje]:
    """Obtiene viajes en una fecha específica."""
    fecha_inicio = datetime(fecha.year, fecha.month, fecha.day, 0, 0, 0)
    fecha_fin = datetime(fecha.year, fecha.month, fecha.day, 23, 59, 59)
    db = SessionLocal()
    try:
        return db.query(Viaje).filter(
            Viaje.fecha_hora_salida >= fecha_inicio,
            Viaje.fecha_hora_salida <= fecha_fin,
        ).all()
    finally:
        db.close()


def actualizar(
    id_viaje: UUID,
    id_usuario_edita: UUID,
    *,
    id_ruta: Optional[UUID] = None,
    id_vehiculo: Optional[UUID] = None,
    id_estacion_origen: Optional[UUID] = None,
    id_estacion_destino: Optional[UUID] = None,
    fecha_hora_salida: Optional[datetime] = None,
) -> Optional[Viaje]:
    """Actualiza un viaje existente."""
    db = SessionLocal()
    try:
        viaje = db.query(Viaje).filter(Viaje.id_viaje == id_viaje).first()
        if not viaje:
            return None
        if id_ruta is not None:
            viaje.id_ruta = id_ruta
        if id_vehiculo is not None:
            viaje.id_vehiculo = id_vehiculo
        if id_estacion_origen is not None:
            viaje.id_estacion_origen = id_estacion_origen
        if id_estacion_destino is not None:
            viaje.id_estacion_destino = id_estacion_destino
        if fecha_hora_salida is not None:
            viaje.fecha_hora_salida = fecha_hora_salida
        viaje.id_usuario_edita = id_usuario_edita
        db.commit()
        db.refresh(viaje)
        return viaje
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def eliminar(id_viaje: UUID) -> bool:
    """Elimina un viaje."""
    db = SessionLocal()
    try:
        viaje = db.query(Viaje).filter(Viaje.id_viaje == id_viaje).first()
        if not viaje:
            return False
        db.delete(viaje)
        db.commit()
        return True
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
