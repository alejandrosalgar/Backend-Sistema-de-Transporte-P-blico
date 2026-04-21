"""
CRUD para la entidad Ruta.
Gestiona líneas o recorridos del sistema de transporte.
Incluye auditoría con usuario creador y editor.
"""

from typing import List, Optional
from uuid import UUID

from src.database.config import SessionLocal
from src.entities.ruta import Ruta


def crear(
    codigo: str,
    id_usuario_creacion: UUID,
    nombre: Optional[str] = None,
    activo: bool = True,
) -> Ruta:
    """Crea una nueva ruta."""
    db = SessionLocal()
    try:
        ruta = Ruta(
            codigo=codigo.strip(),
            nombre=nombre.strip() if nombre else None,
            activo=activo,
            id_usuario_creacion=id_usuario_creacion,
        )
        db.add(ruta)
        db.commit()
        db.refresh(ruta)
        return ruta
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def obtener_por_id(id_ruta: UUID) -> Optional[Ruta]:
    """Obtiene una ruta por su ID."""
    db = SessionLocal()
    try:
        return db.query(Ruta).filter(Ruta.id_ruta == id_ruta).first()
    finally:
        db.close()


def obtener_por_codigo(codigo: str) -> Optional[Ruta]:
    """Obtiene una ruta por su código."""
    db = SessionLocal()
    try:
        return db.query(Ruta).filter(Ruta.codigo == codigo.strip()).first()
    finally:
        db.close()


def obtener_todos() -> List[Ruta]:
    """Obtiene todas las rutas."""
    db = SessionLocal()
    try:
        return db.query(Ruta).all()
    finally:
        db.close()


def obtener_activas() -> List[Ruta]:
    """Obtiene solo las rutas activas."""
    db = SessionLocal()
    try:
        return db.query(Ruta).filter(Ruta.activo == True).all()
    finally:
        db.close()


def actualizar(
    id_ruta: UUID,
    id_usuario_edita: UUID,
    *,
    codigo: Optional[str] = None,
    nombre: Optional[str] = None,
    activo: Optional[bool] = None,
) -> Optional[Ruta]:
    """Actualiza una ruta existente."""
    db = SessionLocal()
    try:
        ruta = db.query(Ruta).filter(Ruta.id_ruta == id_ruta).first()
        if not ruta:
            return None
        if codigo is not None:
            ruta.codigo = codigo.strip()
        if nombre is not None:
            ruta.nombre = nombre.strip()
        if activo is not None:
            ruta.activo = activo
        ruta.id_usuario_edita = id_usuario_edita
        db.commit()
        db.refresh(ruta)
        return ruta
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def eliminar(id_ruta: UUID) -> bool:
    """Elimina una ruta."""
    db = SessionLocal()
    try:
        ruta = db.query(Ruta).filter(Ruta.id_ruta == id_ruta).first()
        if not ruta:
            return False
        db.delete(ruta)
        db.commit()
        return True
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
