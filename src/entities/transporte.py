"""
Módulo que contiene la clase base Transporte.

Clase base que representa un medio de transporte genérico.
Contiene los atributos y comportamientos comunes.
"""


class Transporte:
    """
    Clase base que representa un medio de transporte genérico.

    Contiene los atributos y comportamientos comunes que comparten
    los diferentes tipos de transporte del sistema.
    """

    def __init__(self, marca: str, modelo: str, capacidad: int) -> None:
        """
        Inicializa un objeto Transporte.

        Args:
            marca (str): Marca del transporte.
            modelo (str): Modelo del transporte.
            capacidad (int): Capacidad máxima de pasajeros.
        """
        self._marca = marca
        self._modelo = modelo
        self._capacidad = capacidad

    @property
    def marca(self) -> str:
        """Obtiene la marca del transporte."""
        return self._marca

    @property
    def modelo(self) -> str:
        """Obtiene el modelo del transporte."""
        return self._modelo

    @property
    def capacidad(self) -> int:
        """Obtiene la capacidad del transporte."""
        return self._capacidad

    def imprimir_data(self) -> None:
        """
        Imprime la información básica del transporte.

        Muestra la marca, modelo y capacidad del transporte.
        """
        print(
            f"La marca del transporte es {self._marca}, modelo {self._modelo}, "
            f"y capacidad de {self._capacidad} personas"
        )
