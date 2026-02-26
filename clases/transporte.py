class Transporte:
    """
    Clase base que representa un medio de transporte genérico.

    Contiene los atributos y comportamientos comunes que comparten
    los diferentes tipos de transporte del sistema.
    """

    def __init__(self, marca: str, modelo: str, capacidad: int):
        """
        Inicializa un objeto Transporte.

        Args:
            marca (str): Marca del transporte.
            modelo (str): Modelo del transporte.
            capacidad (int): Capacidad máxima de pasajeros.
        """
        self.marca = marca
        self.modelo = modelo
        self.capacidad = capacidad

    def imprimir_data(self):
        """
        Imprime la información básica del transporte.

        Muestra la marca, modelo y capacidad del transporte.
        """
        print(
            f"La marca del transporte es {self.marca}, modelo {self.modelo}, "
            f"y capacidad de {self.capacidad} personas"
        )
