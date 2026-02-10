class Metro:
    def __init__(self, marca: str, modelo: str, capacidad: int):
        self.marca = marca
        self.modelo = modelo
        self.capacidad = capacidad

    def imprimir_data(self):
        print(
            f"La marca del Metro es {self.marca} , modelo {self.modelo}, y capacidad de {self.capacidad} personas"
        )


metro1 = Metro("toyota", "2010", 50)
metro1.imprimir_data()
