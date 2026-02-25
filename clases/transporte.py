class Transporte:
    def __init__(self, marca: str, modelo: str, capacidad: int):
        self.marca = marca
        self.modelo = modelo
        self.capacidad = capacidad

    def imprimir_data(self):
        print(
            f"La marca del transporte es {self.marca} , modelo {self.modelo}, y capacidad"
            f" de {self.capacidad} personas"
        )
