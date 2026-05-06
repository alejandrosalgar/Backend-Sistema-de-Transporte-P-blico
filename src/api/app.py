"""
API del Sistema de Transporte Público.
Gestiona Usuarios, Tarjetas, Estaciones, Vehículos, Rutas y Viajes.
"""

import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.database.config import create_tables

from . import usuario, tarjeta, estacion, vehiculo, ruta, viaje


def _cors_origins() -> list[str]:
    """Orígenes permitidos: variable ALLOWED_ORIGINS separada por comas. Si está vacía, solo localhost (dev)."""
    raw = os.getenv("ALLOWED_ORIGINS", "").strip()
    if raw:
        return [o.strip() for o in raw.split(",") if o.strip()]
    return [
        "http://localhost:4200",
        "http://127.0.0.1:4200",
    ]


@asynccontextmanager
async def lifespan(_app: FastAPI):
    # Registra modelos y crea tablas si no existen
    import src.entities.usuario  # noqa: F401
    import src.entities.tarjeta  # noqa: F401
    import src.entities.estacion  # noqa: F401
    import src.entities.vehiculo  # noqa: F401
    import src.entities.ruta  # noqa: F401
    import src.entities.viaje  # noqa: F401
    create_tables()
    yield


app = FastAPI(
    title="API Sistema de Transporte Público",
    description="API para gestionar el sistema de transporte público",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=_cors_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(usuario.router)
app.include_router(tarjeta.router)
app.include_router(estacion.router)
app.include_router(vehiculo.router)
app.include_router(ruta.router)
app.include_router(viaje.router)


@app.get("/health")
def health() -> dict[str, str]:
    """Endpoint de salud para verificar que la API está activa."""
    return {"status": "ok"}