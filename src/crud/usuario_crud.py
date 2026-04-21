"""
CRUD para la entidad Usuario.
Incluye creación, login (verificación de contraseña) y operaciones básicas.
"""

import hashlib
from typing import List, Optional
from uuid import UUID

from src.database.config import SessionLocal
from src.entities.usuario import Usuario


def _hash_contrasena(contrasena: str) -> str:
    """Hashea la contraseña con SHA-256 (para no guardar en claro)."""
    return hashlib.sha256(contrasena.encode("utf-8")).hexdigest()


def crear(
    nombre_usuario: str,
    contrasena: str,
    rol: str = "usuario",
    activo: bool = True,
) -> Usuario:
    """Crea un nuevo usuario. La contraseña se hashea antes de guardar."""
    db = SessionLocal()
    try:
        nombre_usuario_limpio = nombre_usuario.strip()
        nombre_usuario_existente = (
            db.query(Usuario)
            .filter(Usuario.nombre_usuario == nombre_usuario_limpio)
            .first()
        )
        if nombre_usuario_existente:
            raise ValueError("El nombre de usuario ya existe")

        usuario = Usuario(
            nombre_usuario=nombre_usuario_limpio,
            contrasena=_hash_contrasena(contrasena),
            rol=rol.strip(),
            activo=activo,
        )
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def login(nombre_usuario: str, contrasena: str) -> Optional[Usuario]:
    """
    Verifica credenciales. Devuelve el Usuario si coincide, None si no.
    """
    db = SessionLocal()
    try:
        usuario = (
            db.query(Usuario)
            .filter(Usuario.nombre_usuario == nombre_usuario.strip())
            .first()
        )
        if not usuario or not usuario.activo:
            return None
        if usuario.contrasena != _hash_contrasena(contrasena):
            return None
        return usuario
    finally:
        db.close()


def obtener_por_id(id_usuario: UUID) -> Optional[Usuario]:
    db = SessionLocal()
    try:
        return db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    finally:
        db.close()


def obtener_por_nombre_usuario(nombre_usuario: str) -> Optional[Usuario]:
    db = SessionLocal()
    try:
        return (
            db.query(Usuario)
            .filter(Usuario.nombre_usuario == nombre_usuario.strip())
            .first()
        )
    finally:
        db.close()


def obtener_todos() -> List[Usuario]:
    db = SessionLocal()
    try:
        return db.query(Usuario).all()
    finally:
        db.close()


def hay_usuarios() -> bool:
    """Indica si existe al menos un usuario (para mostrar opción de registro)."""
    db = SessionLocal()
    try:
        return db.query(Usuario).first() is not None
    finally:
        db.close()


def actualizar(
    id_usuario: UUID,
    *,
    nombre_usuario: Optional[str] = None,
    contrasena: Optional[str] = None,
    rol: Optional[str] = None,
    activo: Optional[bool] = None,
) -> Optional[Usuario]:
    db = SessionLocal()
    try:
        usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        if not usuario:
            return None
        if nombre_usuario is not None:
            usuario.nombre_usuario = nombre_usuario.strip()
        if contrasena is not None:
            usuario.contrasena = _hash_contrasena(contrasena)
        if rol is not None:
            usuario.rol = rol.strip()
        if activo is not None:
            usuario.activo = activo
        db.commit()
        db.refresh(usuario)
        return usuario
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def eliminar(id_usuario: UUID) -> bool:
    db = SessionLocal()
    try:
        usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        if not usuario:
            return False
        db.delete(usuario)
        db.commit()
        return True
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
