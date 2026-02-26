"""
Módulo que contiene la clase Persona.

Clase base para representar a una persona con atributos básicos.
"""


class Persona:
    """
    Clase base para representar una persona.

    Attributes:
        nombre (str): Nombre completo de la persona.
        documento (str): Número de documento de identidad.
        edad (int): Edad de la persona.
        telefono (str): Número de teléfono de contacto.
    """

    def __init__(
        self, nombre: str, documento: str, edad: int, telefono: str
    ) -> None:
        """
        Inicializa una nueva instancia de Persona.

        Args:
            nombre (str): Nombre completo de la persona.
            documento (str): Número de documento de identidad.
            edad (int): Edad de la persona.
            telefono (str): Número de teléfono de contacto.
        """
        self._nombre = nombre
        self._documento = documento
        self._edad = edad
        self._telefono = telefono

    @property
    def nombre(self) -> str:
        """Obtiene el nombre de la persona."""
        return self._nombre

    @property
    def documento(self) -> str:
        """Obtiene el documento de la persona."""
        return self._documento

    @property
    def edad(self) -> int:
        """Obtiene la edad de la persona."""
        return self._edad

    @property
    def telefono(self) -> str:
        """Obtiene el teléfono de la persona."""
        return self._telefono

    def imprimir_data(self) -> None:
        """
        Imprime los datos básicos de la persona.

        Muestra: nombre, documento, edad y teléfono.
        """
        print(
            f"Nombre: {self._nombre}, Documento: {self._documento}, "
            f"Edad: {self._edad}, Teléfono: {self._telefono}"
        )

    @classmethod
    def crear_persona(cls) -> "Persona":
        """
        Método de clase para crear una instancia de Persona por entrada del usuario.

        Returns:
            Persona: Nueva instancia con datos ingresados por el usuario.
        """
        nombre = input("Ingrese el nombre: ")
        documento = input("Ingrese el documento: ")
        edad = int(input("Ingrese la edad: "))
        telefono = input("Ingrese el teléfono: ")
        return cls(nombre, documento, edad, telefono)
