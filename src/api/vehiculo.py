"""
Router para la entidad Vehículo.
Endpoints para crear, obtener, actualizar y eliminar vehículos.
"""

from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from src.crud import vehiculo_crud

router = APIRouter(prefix="/vehiculos", tags=["vehiculos"])


class VehiculoCreate(BaseModel):
    """Esquema para crear un vehículo."""

    placa: str = Field(..., min_length=1, max_length=20)
    modelo: str | None = Field(None, max_length=100)
    capacidad: int | None = Field(None, ge=0)


class VehiculoUpdate(BaseModel):
    """Esquema para actualizar un vehículo."""

    placa: str | None = Field(None, min_length=1, max_length=20)
    modelo: str | None = Field(None, max_length=100)
    capacidad: int | None = Field(None, ge=0)


class VehiculoResponse(BaseModel):
    """Esquema de respuesta para un vehículo."""

    id_vehiculo: UUID
    placa: str
    modelo: str | None
    capacidad: int | None

    class Config:
        from_attributes = True


@router.post("/", response_model=VehiculoResponse, status_code=201)
def crear_vehiculo(vehiculo: VehiculoCreate):
    """Crea un nuevo vehículo."""
    try:
        return vehiculo_crud.crear(
            placa=vehiculo.placa,
            modelo=vehiculo.modelo,
            capacidad=vehiculo.capacidad,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{id_vehiculo}", response_model=VehiculoResponse)
def obtener_vehiculo(id_vehiculo: UUID):
    """Obtiene un vehículo por ID."""
    vehiculo = vehiculo_crud.obtener_por_id(id_vehiculo)
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return vehiculo


@router.get("/", response_model=List[VehiculoResponse])
def obtener_vehiculos():
    """Obtiene todos los vehículos."""
    return vehiculo_crud.obtener_todos()


@router.put("/{id_vehiculo}", response_model=VehiculoResponse)
def actualizar_vehiculo(id_vehiculo: UUID, vehiculo: VehiculoUpdate):
    """Actualiza un vehículo existente."""
    actualizado = vehiculo_crud.actualizar(
        id_vehiculo,
        placa=vehiculo.placa,
        modelo=vehiculo.modelo,
        capacidad=vehiculo.capacidad,
    )
    if not actualizado:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return actualizado


@router.delete("/{id_vehiculo}", status_code=204)
def eliminar_vehiculo(id_vehiculo: UUID):
    """Elimina un vehículo."""
    if not vehiculo_crud.eliminar(id_vehiculo):
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
