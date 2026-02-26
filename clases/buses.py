from clases import transporte


class Bus(transporte.Transporte):
    """
    Clase que representa un Bus dentro del sistema de transporte.

    Hereda de la clase Transporte y añade el atributo específico
    'placa', propio de los buses.
    """

    def __init__(self, marca: str, modelo: str, capacidad: int, placa: str):
        """
        Inicializa un objeto Bus.

        Args:
            marca (str): Marca del bus.
            modelo (str): Modelo del bus.
            capacidad (int): Capacidad máxima de pasajeros.
            placa (str): Placa del bus.
        """
        super().__init__(marca, modelo, capacidad)
        self.placa = placa

    def imprimir_data(self):
        """
        Imprime la información completa del bus en consola.

        Muestra la marca, modelo, capacidad y placa del bus.
        """
        print(
            f"La marca del carro es {self.marca}, modelo {self.modelo}"
            f", capacidad de {self.capacidad} personas, y placa {self.placa}"
        )

    @classmethod
    def añadir_bus(cls):
        """
        Crea un nuevo objeto Bus solicitando los datos al usuario.

        Este método de clase pide por consola la información necesaria
        para crear un nuevo bus y devuelve la instancia creada.

        Returns:
            Bus: Nueva instancia de la clase Bus.
        """
        marca = input("Ingrese la marca del bus: ")
        modelo = input("Ingrese el modelo del bus: ")
        capacidad = int(input("Ingrese la capacidad del bus: "))
        placa = input("Ingrese la placa del bus: ")
        return cls(marca, modelo, capacidad, placa)
