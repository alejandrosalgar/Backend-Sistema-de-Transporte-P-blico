from clases import transporte


class Vector:
    def __init__(self):
        self.transporte = []

    def agregar_transporte(self, transporte: transporte.Transporte):
        self.transporte.append(transporte)

    def mostrar_transporte(self):
        for t in self.transporte:
            t.imprimir_data()
