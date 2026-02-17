from clases import transporte


class Bus(transporte.Transporte):
    def __init__(self, marca: str, modelo: str, capacidad: int, placa: str):
        super().__init__(marca, modelo, capacidad)
        self.placa = placa

    def imprimir_data(self):
        print(
            f"la marca del carro es {self.marca}, modelo {self.modelo}"
            f", capacidad de {self.capacidad} personas, y placa {self.placa}"
        )

    @classmethod
    def añadir_bus(cls):
        marca = input("Ingrese la marca del bus: ")
        modelo = input("Ingrese el modelo del bus: ")
        capacidad = int(input("Ingrese la capacidad del bus: "))
        placa = input("Ingrese la placa del bus: ")
        return cls(marca, modelo, capacidad, placa)
