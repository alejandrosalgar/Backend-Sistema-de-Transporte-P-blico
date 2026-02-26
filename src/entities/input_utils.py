"""
Módulo de utilidades para leer datos saneados desde la entrada estándar.

Contiene funciones que repiten la petición hasta que el usuario provee un valor
válido del tipo esperado (entero o flotante). Esto evita que el programa termine
por un `ValueError` cuando el usuario escribe algo incorrecto.
"""


def solicitar_entero(prompt: str) -> int:
    """Pide un entero por consola hasta que se ingrese uno válido."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número entero.")


def solicitar_flotante(prompt: str) -> float:
    """Pide un número flotante por consola hasta que se ingrese uno válido."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido.")
