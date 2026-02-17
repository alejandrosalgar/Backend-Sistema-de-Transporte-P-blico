from clases import transporte


class Metro(transporte.Transporte):
    def __init__(self, marca: str, modelo: str, capacidad: int, numero_estaciones: int):
        super().__init__(marca, modelo, capacidad)
        self.numero_estaciones = numero_estaciones

    def imprimir_data(self):
        print(
            f"La marca del Metro es {self.marca} , modelo {self.modelo},"
            f"y capacidad de{self.capacidad} personas, con {self.numero_estaciones} estaciones"
        )

    @classmethod
    def añadir_metro(cls):
        marca = input("Ingrese la marca del metro: ")
        modelo = input("Ingrese el modelo del metro: ")
        capacidad = int(input("Ingrese la capacidad del metro: "))
        numero_estaciones = int(input("Ingrese el número de estaciones del metro: "))
        return cls(marca, modelo, capacidad, numero_estaciones)
