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
        self,
        nombre: str,
        documento: str,
        edad: int,
        telefono: str
    ):
        """
        Inicializa una nueva instancia de Persona.

        Args:
            nombre (str): Nombre completo de la persona.
            documento (str): Número de documento de identidad.
            edad (int): Edad de la persona.
            telefono (str): Número de teléfono de contacto.
        """
        self.nombre = nombre
        self.documento = documento
        self.edad = edad
        self.telefono = telefono

    def imprimir_data(self) -> None:
        """
        Imprime los datos básicos de la persona.

        Muestra: nombre, documento, edad y teléfono.
        """
        print(
            f"Nombre: {self.nombre}, Documento: {self.documento}, "
            f"Edad: {self.edad}, Teléfono: {self.telefono}"
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
