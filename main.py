from clases import metro, buses, vector

vector1 = vector.Vector()

while True:
    print("Bienvenido al programa de Sistema de Transporte")
    print("1. Agregar un nuevo metro")
    print("2. Agregar un nuevo bus")
    print("3. Mostrar todos los vehículos")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            metro1 = metro.Metro.añadir_metro()
            vector1.agregar_transporte(metro1)
        case "2":
            bus1 = buses.Bus.añadir_bus()
            vector1.agregar_transporte(bus1)
        case "3":
            vector1.mostrar_transporte()
        case "0":
            print("Gracias por usar el programa de Sistema de Transporte")
            break
        case _:
            print("Opción no válida, por favor seleccione una opción del 1 al 4")
