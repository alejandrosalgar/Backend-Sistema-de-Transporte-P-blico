"""
Módulo que contiene la clase Metro.

Clase que representa un Metro dentro del sistema de transporte.
"""

from src.entities.transporte import Transporte


class Metro(Transporte):
    """
    Clase que representa un Metro dentro del sistema de transporte.

    Hereda de la clase Transporte y añade el atributo específico
    'numero_estaciones', propio del sistema de metro.
    """

    def __init__(
        self, marca: str, modelo: str, capacidad: int, numero_estaciones: int
    ) -> None:
        """
        Inicializa un objeto Metro.

        Args:
            marca (str): Marca del metro.
            modelo (str): Modelo del metro.
            capacidad (int): Capacidad máxima de pasajeros.
            numero_estaciones (int): Número de estaciones que recorre.
        """
        super().__init__(marca, modelo, capacidad)
        self._numero_estaciones = numero_estaciones

    @property
    def numero_estaciones(self) -> int:
        """Obtiene el número de estaciones del metro."""
        return self._numero_estaciones

    def imprimir_data(self) -> None:
        """
        Imprime la información completa del metro en consola.

        Muestra la marca, modelo, capacidad y número de estaciones.
        """
        print(
            f"La marca del Metro es {self.marca}, modelo {self.modelo}, "
            f"capacidad de {self.capacidad} personas, "
            f"con {self._numero_estaciones} estaciones"
        )

    @classmethod
    def añadir_metro(cls) -> "Metro":
        """
        Crea un nuevo objeto Metro solicitando los datos al usuario.

        Los valores numéricos se capturan mediante utilidades que repiten la
        pregunta hasta recibir un entero válido. Esto evita cierres inesperados
        por entradas no numéricas.

        Returns:
            Metro: Nueva instancia de la clase Metro.
        """
        from src.entities.input_utils import solicitar_entero

        marca = input("Ingrese la marca del metro: ")
        modelo = input("Ingrese el modelo del metro: ")
        capacidad = solicitar_entero("Ingrese la capacidad del metro: ")
        numero_estaciones = solicitar_entero(
            "Ingrese el número de estaciones del metro: "
        )
        return cls(marca, modelo, capacidad, numero_estaciones)
