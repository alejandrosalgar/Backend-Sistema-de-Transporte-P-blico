"""
Módulo que contiene la clase Vector.

Clase que administra una colección de objetos Transporte.
"""

from src.entities.transporte import Transporte


class Vector:
    """
    Clase que administra una colección de objetos Transporte.

    Permite agregar transportes al sistema y mostrar la información
    de todos los transportes almacenados.
    """

    def __init__(self) -> None:
        """Inicializa el vector (lista) de transportes vacío."""
        self._transportes: list = []

    @property
    def transportes(self) -> list:
        """Obtiene la lista de transportes."""
        return self._transportes

    def agregar_transporte(self, transporte: Transporte) -> None:
        """
        Agrega un objeto Transporte a la lista.

        Args:
            transporte (Transporte): Instancia de la clase Transporte
                                     o cualquiera de sus clases hijas
                                     (Bus, Metro, etc.).
        """
        self._transportes.append(transporte)

    def mostrar_transporte(self) -> None:
        """
        Recorre la lista de transportes e imprime la información
        de cada uno utilizando polimorfismo.
        """
        for t in self._transportes:
            t.imprimir_data()
