"""
Router para la entidad Estación.
Endpoints para crear, obtener, actualizar y eliminar estaciones.
"""

from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from src.crud import estacion_crud

router = APIRouter(prefix="/estaciones", tags=["estaciones"])


class EstacionCreate(BaseModel):
    """Esquema para crear una estación."""

    nombre: str = Field(..., min_length=1, max_length=150)
    direccion: str | None = Field(None, max_length=255)


class EstacionUpdate(BaseModel):
    """Esquema para actualizar una estación."""

    nombre: str | None = Field(None, min_length=1, max_length=150)
    direccion: str | None = Field(None, max_length=255)


class EstacionResponse(BaseModel):
    """Esquema de respuesta para una estación."""

    id_estacion: UUID
    nombre: str
    direccion: str | None

    class Config:
        from_attributes = True


@router.post("/", response_model=EstacionResponse, status_code=201)
def crear_estacion(estacion: EstacionCreate):
    """Crea una nueva estación."""
    try:
        return estacion_crud.crear(
            nombre=estacion.nombre,
            direccion=estacion.direccion,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{id_estacion}", response_model=EstacionResponse)
def obtener_estacion(id_estacion: UUID):
    """Obtiene una estación por ID."""
    estacion = estacion_crud.obtener_por_id(id_estacion)
    if not estacion:
        raise HTTPException(status_code=404, detail="Estación no encontrada")
    return estacion


@router.get("/", response_model=List[EstacionResponse])
def obtener_estaciones():
    """Obtiene todas las estaciones."""
    return estacion_crud.obtener_todos()


@router.put("/{id_estacion}", response_model=EstacionResponse)
def actualizar_estacion(id_estacion: UUID, estacion: EstacionUpdate):
    """Actualiza una estación existente."""
    actualizada = estacion_crud.actualizar(
        id_estacion,
        nombre=estacion.nombre,
        direccion=estacion.direccion,
    )
    if not actualizada:
        raise HTTPException(status_code=404, detail="Estación no encontrada")
    return actualizada


@router.delete("/{id_estacion}", status_code=204)
def eliminar_estacion(id_estacion: UUID):
    """Elimina una estación."""
    if not estacion_crud.eliminar(id_estacion):
        raise HTTPException(status_code=404, detail="Estación no encontrada")
