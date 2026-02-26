"""
Paquete entities del Sistema de Transporte Público.

Exporta todas las clases del módulo entities.
"""

from src.entities.transporte import Transporte
from src.entities.persona import Persona
from src.entities.metro import Metro
from src.entities.buses import Bus
from src.entities.usuario import Usuario
from src.entities.vector import Vector

__all__ = [
    "Transporte",
    "Persona",
    "Metro",
    "Bus",
    "Usuario",
    "Vector",
]
