"""
Módulo que contiene la clase Usuario.

Clase para representar un usuario del sistema de transporte público.
"""

from clases import persona


class Usuario(persona.Persona):
    """
    Clase que representa un usuario del sistema de transporte.

    Hereda de Persona y agrega funcionalidades de tarjeta y compras.

    Attributes:
        nombre (str): Nombre completo del usuario.
        documento (str): Número de documento de identidad.
        edad (int): Edad del usuario.
        telefono (str): Número de teléfono de contacto.
        saldo (float): Saldo disponible en la tarjeta.
        historial_compras (list): Lista de compras realizadas.
    """

    def __init__(
        self,
        nombre: str,
        documento: str,
        edad: int,
        telefono: str,
        saldo: float = 0.0
    ):
        """
        Inicializa una nueva instancia de Usuario.

        Args:
            nombre (str): Nombre completo del usuario.
            documento (str): Número de documento de identidad.
            edad (int): Edad del usuario.
            telefono (str): Número de teléfono de contacto.
            saldo (float): Saldo inicial en la tarjeta. Default: 0.0
        """
        super().__init__(nombre, documento, edad, telefono)
        self.saldo = saldo
        self.historial_compras = []

    def consultar_saldo(self) -> float:
        """
        Consulta el saldo actual de la tarjeta del usuario.

        Returns:
            float: Saldo disponible en la tarjeta.
        """
        return self.saldo

    def recargar_tarjeta(self, monto: float) -> bool:
        """
        Recarga el saldo de la tarjeta del usuario.

        Args:
            monto (float): Cantidad a recargar en la tarjeta.

        Returns:
            bool: True si la recarga fue exitosa, False en caso contrario.

        Raises:
            ValueError: Si el monto es negativo o cero.
        """
        if monto <= 0:
            raise ValueError("El monto a recargar debe ser positivo")

        self.saldo += monto
        self.historial_compras.append(
            {
                "tipo": "recarga",
                "monto": monto,
                "saldo_resultante": self.saldo
            }
        )
        return True

    def registrar_compra(self, transporte_tipo: str, monto: float) -> bool:
        """
        Registra una compra de pasaje en el historial del usuario.

        Args:
            transporte_tipo (str): Tipo de transporte (bus, metro, tranvía).
            monto (float): Costo del pasaje.

        Returns:
            bool: True si la compra fue exitosa, False si no hay saldo suficiente.

        Raises:
            ValueError: Si el monto es negativo o cero.
        """
        if monto <= 0:
            raise ValueError("El monto del pasaje debe ser positivo")

        if self.saldo < monto:
            print(f"Saldo insuficiente. Saldo actual: ${self.saldo}")
            return False

        self.saldo -= monto
        self.historial_compras.append(
            {
                "tipo": "compra",
                "transporte": transporte_tipo,
                "monto": monto,
                "saldo_resultante": self.saldo
            }
        )
        return True

    def obtener_historial(self) -> list:
        """
        Obtiene el historial completo de compras y recargas.

        Returns:
            list: Lista de diccionarios con el historial de transacciones.
        """
        return self.historial_compras

    def imprimir_data(self) -> None:
        """
        Imprime los datos del usuario incluyendo saldo actual.

        Muestra: nombre, documento, edad, teléfono y saldo.
        """
        print(
            f"Nombre: {self.nombre}, Documento: {self.documento}, "
            f"Edad: {self.edad}, Teléfono: {self.telefono}, "
            f"Saldo: ${self.saldo:.2f}"
        )

    @classmethod
    def crear_usuario(cls) -> "Usuario":
        """
        Método de clase para crear una instancia de Usuario por entrada del usuario.

        Solicita entrada del usuario para nombre, documento, edad, teléfono y saldo.

        Returns:
            Usuario: Nueva instancia con datos ingresados por el usuario.
        """
        nombre = input("Ingrese el nombre: ")
        documento = input("Ingrese el documento: ")
        edad = int(input("Ingrese la edad: "))
        telefono = input("Ingrese el teléfono: ")
        saldo = float(input("Ingrese el saldo inicial (opcional, default 0): ") or 0)
        return cls(nombre, documento, edad, telefono, saldo)
