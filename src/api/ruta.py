"""
Router para la entidad Ruta.
Endpoints para crear, obtener, actualizar y eliminar rutas.
"""

from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from src.crud import ruta_crud

router = APIRouter(prefix="/rutas", tags=["rutas"])


class RutaCreate(BaseModel):
    """Esquema para crear una ruta."""
    codigo: str = Field(..., min_length=1, max_length=20)
    nombre: str | None = Field(None, max_length=150)
    activo: bool = True
    id_usuario_creacion: UUID


class RutaUpdate(BaseModel):
    """Esquema para actualizar una ruta."""
    codigo: str | None = Field(None, min_length=1, max_length=20)
    nombre: str | None = Field(None, max_length=150)
    activo: bool | None = None
    id_usuario_edita: UUID


class RutaResponse(BaseModel):
    """Esquema de respuesta para una ruta."""
    id_ruta: UUID
    codigo: str
    nombre: str | None
    activo: bool

    class Config:
        from_attributes = True


@router.post("/", response_model=RutaResponse, status_code=201)
def crear_ruta(ruta: RutaCreate):
    """Crea una nueva ruta."""
    try:
        return ruta_crud.crear(
            codigo=ruta.codigo,
            nombre=ruta.nombre,
            activo=ruta.activo,
            id_usuario_creacion=ruta.id_usuario_creacion,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{id_ruta}", response_model=RutaResponse)
def obtener_ruta(id_ruta: UUID):
    """Obtiene una ruta por ID."""
    ruta = ruta_crud.obtener_por_id(id_ruta)
    if not ruta:
        raise HTTPException(status_code=404, detail="Ruta no encontrada")
    return ruta


@router.get("/", response_model=List[RutaResponse])
def obtener_rutas():
    """Obtiene todas las rutas."""
    return ruta_crud.obtener_todos()


@router.get("/activas", response_model=List[RutaResponse])
def obtener_rutas_activas():
    """Obtiene solo las rutas activas."""
    return ruta_crud.obtener_activas()


@router.get("/codigo/{codigo}", response_model=RutaResponse)
def obtener_ruta_por_codigo(codigo: str):
    """Obtiene una ruta por su código."""
    ruta = ruta_crud.obtener_por_codigo(codigo)
    if not ruta:
        raise HTTPException(status_code=404, detail="Ruta no encontrada")
    return ruta


@router.put("/{id_ruta}", response_model=RutaResponse)
def actualizar_ruta(id_ruta: UUID, ruta: RutaUpdate):
    """Actualiza una ruta existente."""
    actualizada = ruta_crud.actualizar(
        id_ruta,
        ruta.id_usuario_edita,
        codigo=ruta.codigo,
        nombre=ruta.nombre,
        activo=ruta.activo,
    )
    if not actualizada:
        raise HTTPException(status_code=404, detail="Ruta no encontrada")
    return actualizada
