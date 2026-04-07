"""
Router para la entidad Usuario.
Endpoints para crear, obtener, actualizar y eliminar usuarios.
"""

from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr, Field

from src.crud import usuario_crud

router = APIRouter(prefix="/usuarios", tags=["usuarios"])


class UsuarioCreate(BaseModel):
    """Esquema para crear un usuario."""
    nombre_usuario: str = Field(..., min_length=1, max_length=150)
    contrasena: str = Field(..., min_length=6)
    rol: str = Field(default="usuario", max_length=50)
    activo: bool = True


class UsuarioUpdate(BaseModel):
    """Esquema para actualizar un usuario."""
    nombre_usuario: str | None = Field(None, min_length=1, max_length=150)
    contrasena: str | None = Field(None, min_length=6)
    rol: str | None = Field(None, max_length=50)
    activo: bool | None = None


class UsuarioResponse(BaseModel):
    """Esquema de respuesta para un usuario."""
    id_usuario: UUID
    nombre_usuario: str
    rol: str
    activo: bool

    class Config:
        from_attributes = True


@router.post("/", response_model=UsuarioResponse, status_code=201)
def crear_usuario(usuario: UsuarioCreate):
    """Crea un nuevo usuario."""
    try:
        return usuario_crud.crear(
            nombre_usuario=usuario.nombre_usuario,
            contrasena=usuario.contrasena,
            rol=usuario.rol,
            activo=usuario.activo,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{id_usuario}", response_model=UsuarioResponse)
def obtener_usuario(id_usuario: UUID):
    """Obtiene un usuario por ID."""
    usuario = usuario_crud.obtener_por_id(id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


@router.get("/", response_model=List[UsuarioResponse])
def obtener_usuarios():
    """Obtiene todos los usuarios."""
    return usuario_crud.obtener_todos()


@router.put("/{id_usuario}", response_model=UsuarioResponse)
def actualizar_usuario(id_usuario: UUID, usuario: UsuarioUpdate):
    """Actualiza un usuario existente."""
    actualizado = usuario_crud.actualizar(
        id_usuario,
        nombre_usuario=usuario.nombre_usuario,
        contrasena=usuario.contrasena,
        rol=usuario.rol,
        activo=usuario.activo,
    )
    if not actualizado:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return actualizado


@router.post("/login")
def login(nombre_usuario: str, contrasena: str):
    """Verifica credenciales del usuario."""
    usuario = usuario_crud.login(nombre_usuario, contrasena)
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return {"id_usuario": usuario.id_usuario, "nombre_usuario": usuario.nombre_usuario, "rol": usuario.rol}
