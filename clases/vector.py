from clases import transporte


class Vector:
    """
    Clase que administra una colección de objetos Transporte.

    Permite agregar transportes al sistema y mostrar la información
    de todos los transportes almacenados.
    """

    def __init__(self):
        """
        Inicializa el vector (lista) de transportes vacío.
        """
        self.transporte = []

    def agregar_transporte(self, transporte: transporte.Transporte):
        """
        Agrega un objeto Transporte a la lista.

        Args:
            transporte (Transporte): Instancia de la clase Transporte
                                     o cualquiera de sus clases hijas
                                     (Bus, Metro, etc.).
        """
        self.transporte.append(transporte)

    def mostrar_transporte(self):
        """
        Recorre la lista de transportes e imprime la información
        de cada uno utilizando polimorfismo.
        """
        for t in self.transporte:
            t.imprimir_data()
