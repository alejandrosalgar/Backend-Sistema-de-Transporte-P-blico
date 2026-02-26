from clases import transporte


class Metro(transporte.Transporte):
    """
    Clase que representa un Metro dentro del sistema de transporte.

    Hereda de la clase Transporte y añade el atributo específico
    'numero_estaciones', propio del sistema de metro.
    """

    def __init__(self, marca: str, modelo: str, capacidad: int, numero_estaciones: int):
        """
        Inicializa un objeto Metro.

        Args:
            marca (str): Marca del metro.
            modelo (str): Modelo del metro.
            capacidad (int): Capacidad máxima de pasajeros.
            numero_estaciones (int): Número de estaciones que recorre.
        """
        super().__init__(marca, modelo, capacidad)
        self.numero_estaciones = numero_estaciones

    def imprimir_data(self):
        """
        Imprime la información completa del metro en consola.

        Muestra la marca, modelo, capacidad y número de estaciones.
        """
        print(
            f"La marca del Metro es {self.marca}, modelo {self.modelo}, "
            f"capacidad de {self.capacidad} personas, "
            f"con {self.numero_estaciones} estaciones"
        )

    @classmethod
    def añadir_metro(cls):
        """
        Crea un nuevo objeto Metro solicitando los datos al usuario.

        Este método de clase pide por consola la información necesaria
        para crear un nuevo metro y devuelve la instancia creada.

        Returns:
            Metro: Nueva instancia de la clase Metro.
        """
        marca = input("Ingrese la marca del metro: ")
        modelo = input("Ingrese el modelo del metro: ")
        capacidad = int(input("Ingrese la capacidad del metro: "))
        numero_estaciones = int(input("Ingrese el número de estaciones del metro: "))
        return cls(marca, modelo, capacidad, numero_estaciones)
