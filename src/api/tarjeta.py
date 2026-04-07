"""
Router para la entidad Tarjeta.
Endpoints para crear, obtener, actualizar y eliminar tarjetas de transporte.
"""

from typing import List
from uuid import UUID
from decimal import Decimal

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from src.crud import tarjeta_crud

router = APIRouter(prefix="/tarjetas", tags=["tarjetas"])


class TarjetaCreate(BaseModel):
    """Esquema para crear una tarjeta."""
    saldo: Decimal = Field(..., gt=0)
    tipo: str | None = None
    activo: bool = True
    id_usuario: UUID
    id_usuario_creacion: UUID


class TarjetaUpdate(BaseModel):
    """Esquema para actualizar una tarjeta."""
    saldo: Decimal | None = Field(None, gt=0)
    tipo: str | None = None
    activo: bool | None = None
    id_usuario_edita: UUID


class TarjetaResponse(BaseModel):
    """Esquema de respuesta para una tarjeta."""
    id_tarjeta: UUID
    saldo: Decimal
    tipo: str | None
    activo: bool
    id_usuario: UUID

    class Config:
        from_attributes = True


@router.post("/", response_model=TarjetaResponse, status_code=201)
def crear_tarjeta(tarjeta: TarjetaCreate):
    """Crea una nueva tarjeta."""
    try:
        return tarjeta_crud.crear(
            saldo=tarjeta.saldo,
            tipo=tarjeta.tipo,
            activo=tarjeta.activo,
            id_usuario=tarjeta.id_usuario,
            id_usuario_creacion=tarjeta.id_usuario_creacion,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{id_tarjeta}", response_model=TarjetaResponse)
def obtener_tarjeta(id_tarjeta: UUID):
    """Obtiene una tarjeta por ID."""
    tarjeta = tarjeta_crud.obtener_por_id(id_tarjeta)
    if not tarjeta:
        raise HTTPException(status_code=404, detail="Tarjeta no encontrada")
    return tarjeta


@router.get("/", response_model=List[TarjetaResponse])
def obtener_tarjetas():
    """Obtiene todas las tarjetas."""
    return tarjeta_crud.obtener_todos()


@router.get("/usuario/{id_usuario}", response_model=List[TarjetaResponse])
def obtener_tarjetas_por_usuario(id_usuario: UUID):
    """Obtiene todas las tarjetas de un usuario."""
    return tarjeta_crud.obtener_por_usuario(id_usuario)


@router.put("/{id_tarjeta}", response_model=TarjetaResponse)
def actualizar_tarjeta(id_tarjeta: UUID, tarjeta: TarjetaUpdate):
    """Actualiza una tarjeta existente."""
    actualizada = tarjeta_crud.actualizar(
        id_tarjeta,
        tarjeta.id_usuario_edita,
        saldo=tarjeta.saldo,
        tipo=tarjeta.tipo,
        activo=tarjeta.activo,
    )
    if not actualizada:
        raise HTTPException(status_code=404, detail="Tarjeta no encontrada")
    return actualizada


@router.delete("/{id_tarjeta}", status_code=204)
def eliminar_tarjeta(id_tarjeta: UUID):
    """Elimina una tarjeta."""
    if not tarjeta_crud.eliminar(id_tarjeta):
        raise HTTPException(status_code=404, detail="Tarjeta no encontrada")
