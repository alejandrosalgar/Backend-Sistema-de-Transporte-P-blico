"""
Router para la entidad Viaje.
Endpoints para crear, obtener, actualizar y eliminar viajes.
"""

from typing import List
from uuid import UUID
from datetime import datetime

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from src.crud import viaje_crud

router = APIRouter(prefix="/viajes", tags=["viajes"])


class ViajeCreate(BaseModel):
    """Esquema para crear un viaje."""
    id_ruta: UUID
    id_vehiculo: UUID
    id_estacion_origen: UUID
    id_estacion_destino: UUID
    fecha_hora_salida: datetime
    id_usuario_creacion: UUID


class ViajeUpdate(BaseModel):
    """Esquema para actualizar un viaje."""
    id_ruta: UUID | None = None
    id_vehiculo: UUID | None = None
    id_estacion_origen: UUID | None = None
    id_estacion_destino: UUID | None = None
    fecha_hora_salida: datetime | None = None
    id_usuario_edita: UUID


class ViajeResponse(BaseModel):
    """Esquema de respuesta para un viaje."""
    id_viaje: UUID
    id_ruta: UUID
    id_vehiculo: UUID
    id_estacion_origen: UUID
    id_estacion_destino: UUID
    fecha_hora_salida: datetime

    class Config:
        from_attributes = True


@router.post("/", response_model=ViajeResponse, status_code=201)
def crear_viaje(viaje: ViajeCreate):
    """Crea un nuevo viaje."""
    try:
        return viaje_crud.crear(
            id_ruta=viaje.id_ruta,
            id_vehiculo=viaje.id_vehiculo,
            id_estacion_origen=viaje.id_estacion_origen,
            id_estacion_destino=viaje.id_estacion_destino,
            fecha_hora_salida=viaje.fecha_hora_salida,
            id_usuario_creacion=viaje.id_usuario_creacion,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{id_viaje}", response_model=ViajeResponse)
def obtener_viaje(id_viaje: UUID):
    """Obtiene un viaje por ID."""
    viaje = viaje_crud.obtener_por_id(id_viaje)
    if not viaje:
        raise HTTPException(status_code=404, detail="Viaje no encontrado")
    return viaje


@router.get("/", response_model=List[ViajeResponse])
def obtener_viajes():
    """Obtiene todos los viajes."""
    return viaje_crud.obtener_todos()


@router.get("/ruta/{id_ruta}", response_model=List[ViajeResponse])
def obtener_viajes_por_ruta(id_ruta: UUID):
    """Obtiene todos los viajes de una ruta."""
    return viaje_crud.obtener_por_ruta(id_ruta)


@router.get("/vehiculo/{id_vehiculo}", response_model=List[ViajeResponse])
def obtener_viajes_por_vehiculo(id_vehiculo: UUID):
    """Obtiene todos los viajes de un vehículo."""
    return viaje_crud.obtener_por_vehiculo(id_vehiculo)


@router.get("/estacion/origen/{id_estacion}", response_model=List[ViajeResponse])
def obtener_viajes_por_estacion_origen(id_estacion: UUID):
    """Obtiene todos los viajes que salen de una estación."""
    return viaje_crud.obtener_por_estacion_origen(id_estacion)


@router.get("/estacion/destino/{id_estacion}", response_model=List[ViajeResponse])
def obtener_viajes_por_estacion_destino(id_estacion: UUID):
    """Obtiene todos los viajes que llegan a una estación."""
    return viaje_crud.obtener_por_estacion_destino(id_estacion)


@router.put("/{id_viaje}", response_model=ViajeResponse)
def actualizar_viaje(id_viaje: UUID, viaje: ViajeUpdate):
    """Actualiza un viaje existente."""
    actualizado = viaje_crud.actualizar(
        id_viaje,
        viaje.id_usuario_edita,
        id_ruta=viaje.id_ruta,
        id_vehiculo=viaje.id_vehiculo,
        id_estacion_origen=viaje.id_estacion_origen,
        id_estacion_destino=viaje.id_estacion_destino,
        fecha_hora_salida=viaje.fecha_hora_salida,
    )
    if not actualizado:
        raise HTTPException(status_code=404, detail="Viaje no encontrado")
    return actualizado


@router.delete("/{id_viaje}", status_code=204)
def eliminar_viaje(id_viaje: UUID):
    """Elimina un viaje."""
    if not viaje_crud.eliminar(id_viaje):
        raise HTTPException(status_code=404, detail="Viaje no encontrado")
