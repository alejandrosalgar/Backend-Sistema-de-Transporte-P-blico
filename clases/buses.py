class Bus:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def imprimir_data(self):
        print(f"la marca del carro es {self.marca} y el modelo es {self.modelo}")
