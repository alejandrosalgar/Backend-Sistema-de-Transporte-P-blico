class Bus:
    def __init__(self, marca: str, modelo: str, capacidad: int):
        self.marca = marca
        self.modelo = modelo
        self.capacidad = capacidad

    def imprimir_data(self):
        print(f"la marca del carro es {self.marca} y el modelo es {self.modelo}")
