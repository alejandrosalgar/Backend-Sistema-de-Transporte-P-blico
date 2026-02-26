"""
Módulo principal del Sistema de Transporte Público.

Este archivo contiene el menú interactivo del programa,
permitiendo al usuario gestionar vehículos (Metro y Bus)
y realizar operaciones relacionadas con usuarios como
recarga de saldo y compra de pasajes.

Funcionalidades principales:
- Agregar nuevos vehículos.
- Mostrar lista de vehículos registrados.
- Crear usuarios.
- Recargar saldo.
- Registrar compra de pasajes.
- Mostrar historial de compras.
"""

from src.entities import Metro, Bus, Vector, Usuario
from src.entities.input_utils import solicitar_entero, solicitar_flotante

# Instancia principal que administra la lista de transportes
vector1 = Vector()
usuario1 = None

while True:
    print("Bienvenido al programa de Sistema de Transporte")
    print("1. Agregar un nuevo metro")
    print("2. Agregar un nuevo bus")
    print("3. Mostrar todos los vehículos")
    print("4. Añadir usuario")
    print("5. Recargar saldo a usuario")
    print("6. Registrar compra de pasaje")
    print("7. Mostrar historial de compras del usuario")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            # Crear y agregar un nuevo metro al sistema
            metro1 = Metro.añadir_metro()
            vector1.agregar_transporte(metro1)

        case "2":
            # Crear y agregar un nuevo bus al sistema
            bus1 = Bus.añadir_bus()
            vector1.agregar_transporte(bus1)

        case "3":
            # Mostrar todos los vehículos registrados
            vector1.mostrar_transporte()

        case "4":
            # Crear un nuevo usuario
            usuario1 = Usuario.crear_usuario()

        case "5":
            # Recargar saldo del usuario
            if usuario1 is None:
                print("Debe crear un usuario primero (opción 4)")
            else:
                monto = solicitar_flotante("Ingrese el monto a recargar: ")
                try:
                    usuario1.recargar_tarjeta(monto)
                except ValueError as e:
                    print("Error de recarga:", e)

        case "6":
            # Registrar compra de pasaje
            if usuario1 is None:
                print("Debe crear un usuario primero (opción 4)")
            else:
                transporte_tipo = input(
                    "Ingrese el tipo de transporte (bus, metro, tranvía): "
                )
                monto = solicitar_flotante("Ingrese el costo del pasaje: ")
                try:
                    usuario1.registrar_compra(transporte_tipo, monto)
                except ValueError as e:
                    print("Error en compra:", e)

        case "7":
            # Mostrar historial de compras del usuario
            if usuario1 is None:
                print("Debe crear un usuario primero (opción 4)")
            else:
                print("Historial de compras del usuario:")
                for compra in usuario1.historial_compras:
                    print(compra)

        case "0":
            # Salir del programa
            print("Gracias por usar el programa de Sistema de Transporte")
            break

        case _:
            # Manejo de opción inválida
            print("Opción no válida, por favor seleccione una opción válida")
