"""
Módulo principal del Sistema de Transporte Público.
Menú interactivo para gestionar Usuarios, Tarjetas, Estaciones, Vehículos, Rutas y Viajes.
"""

from datetime import datetime
from src.crud import (
    usuario_crud,
    tarjeta_crud,
    estacion_crud,
    vehiculo_crud,
    ruta_crud,
    viaje_crud,
)
from uuid import UUID


def menu_principal():
    while True:
        print("\n===== SISTEMA DE TRANSPORTE PÚBLICO =====")
        print("1. Gestión de Usuarios")
        print("2. Gestión de Tarjetas")
        print("3. Gestión de Estaciones")
        print("4. Gestión de Vehículos")
        print("5. Gestión de Rutas")
        print("6. Gestión de Viajes")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_usuarios()
        elif opcion == "2":
            menu_tarjetas()
        elif opcion == "3":
            menu_estaciones()
        elif opcion == "4":
            menu_vehiculos()
        elif opcion == "5":
            menu_rutas()
        elif opcion == "6":
            menu_viajes()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")


def menu_usuarios():
    while True:
        print("\n--- USUARIOS ---")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Editar usuario")
        print("4. Eliminar usuario")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre de usuario: ")
            contrasena = input("Contraseña: ")
            rol = input("Rol (usuario/admin): ")
            try:
                u = usuario_crud.crear(nombre, contrasena, rol)
                print(f"Usuario creado. ID: {u.id_usuario}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            usuarios = usuario_crud.obtener_todos()
            if not usuarios:
                print("No hay usuarios registrados.")
            for u in usuarios:
                print(
                    f"ID: {u.id_usuario} | Usuario: {u.nombre_usuario} | Rol: {u.rol} | Activo: {u.activo}"
                )

        elif opcion == "3":
            id_str = input("ID del usuario a editar: ")
            try:
                id_usuario = UUID(id_str)
                nombre = input("Nuevo nombre de usuario (Enter para omitir): ") or None
                contrasena = input("Nueva contraseña (Enter para omitir): ") or None
                rol = input("Nuevo rol (Enter para omitir): ") or None
                u = usuario_crud.actualizar(
                    id_usuario, nombre_usuario=nombre, contrasena=contrasena, rol=rol
                )
                if u:
                    print(f"Usuario actualizado: {u.nombre_usuario}")
                else:
                    print("Usuario no encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcion == "4":
            id_str = input("ID del usuario a eliminar: ")
            try:
                id_usuario = UUID(id_str)
                ok = usuario_crud.eliminar(id_usuario)
                print("Usuario eliminado." if ok else "Usuario no encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcion == "0":
            break
        else:
            print("Opción no válida.")


def menu_tarjetas():
    while True:
        print("\n--- TARJETAS ---")
        print("1. Crear tarjeta")
        print("2. Listar tarjetas")
        print("3. Editar tarjeta")
        print("4. Eliminar tarjeta")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                saldo = float(input("Saldo inicial: "))
                tipo = input("Tipo (personal/empresarial): ")
                id_usuario_str = input("ID del usuario dueño de la tarjeta: ")
                id_usuario = UUID(id_usuario_str)
                t = tarjeta_crud.crear(
                    saldo=saldo, id_usuario=id_usuario, id_usuario_creacion=id_usuario
                )
                print(f"Tarjeta creada. ID: {t.id_tarjeta}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            tarjetas = tarjeta_crud.obtener_todos()
            if not tarjetas:
                print("No hay tarjetas registradas.")
            for t in tarjetas:
                print(
                    f"ID: {t.id_tarjeta} | Saldo: {t.saldo} | Tipo: {t.tipo} | Activo: {t.activo} | Usuario: {t.id_usuario}"
                )

        elif opcion == "3":
            try:
                id_str = input("ID de la tarjeta a editar: ")
                id_tarjeta = UUID(id_str)
                id_editor_str = input("ID del usuario que edita: ")
                id_usuario_edita = UUID(id_editor_str)
                saldo_str = input("Nuevo saldo (Enter para omitir): ")
                tipo = input("Nuevo tipo (Enter para omitir): ") or None
                kwargs = {}
                if saldo_str:
                    kwargs["saldo"] = float(saldo_str)
                if tipo:
                    kwargs["tipo"] = tipo
                t = tarjeta_crud.actualizar(id_tarjeta, id_usuario_edita, **kwargs)
                if t:
                    print(f"Tarjeta actualizada. Saldo: {t.saldo}")
                else:
                    print("Tarjeta no encontrada.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "4":
            id_str = input("ID de la tarjeta a eliminar: ")
            try:
                id_tarjeta = UUID(id_str)
                ok = tarjeta_crud.eliminar(id_tarjeta)
                print("Tarjeta eliminada." if ok else "Tarjeta no encontrada.")
            except ValueError:
                print("ID inválido.")

        elif opcion == "0":
            break
        else:
            print("Opción no válida.")


def menu_estaciones():
    while True:
        print("\n--- ESTACIONES ---")
        print("1. Crear estación")
        print("2. Listar estaciones")
        print("3. Editar estación")
        print("4. Eliminar estación")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la estación: ")
            direccion = input("Dirección (Enter para omitir): ") or None
            try:
                e = estacion_crud.crear(nombre, direccion)
                print(f"Estación creada. ID: {e.id_estacion}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            estaciones = estacion_crud.obtener_todos()
            if not estaciones:
                print("No hay estaciones registradas.")
            for e in estaciones:
                print(
                    f"ID: {e.id_estacion} | Nombre: {e.nombre} | Dirección: {e.direccion}"
                )

        elif opcion == "3":
            id_str = input("ID de la estación a editar: ")
            try:
                id_estacion = UUID(id_str)
                nombre = input("Nuevo nombre (Enter para omitir): ") or None
                direccion = input("Nueva dirección (Enter para omitir): ") or None
                e = estacion_crud.actualizar(
                    id_estacion, nombre=nombre, direccion=direccion
                )
                if e:
                    print(f"Estación actualizada: {e.nombre}")
                else:
                    print("Estación no encontrada.")
            except ValueError:
                print("ID inválido.")

        elif opcion == "4":
            id_str = input("ID de la estación a eliminar: ")
            try:
                id_estacion = UUID(id_str)
                ok = estacion_crud.eliminar(id_estacion)
                print("Estación eliminada." if ok else "Estación no encontrada.")
            except ValueError:
                print("ID inválido.")

        elif opcion == "0":
            break
        else:
            print("Opción no válida.")


def menu_vehiculos():
    while True:
        print("\n--- VEHÍCULOS ---")
        print("1. Crear vehículo")
        print("2. Listar vehículos")
        print("3. Editar vehículo")
        print("4. Eliminar vehículo")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            placa = input("Placa del vehículo: ")
            modelo = input("Modelo (Enter para omitir): ") or None
            capacidad_str = input("Capacidad (Enter para omitir): ") or None
            try:
                capacidad = int(capacidad_str) if capacidad_str else None
                v = vehiculo_crud.crear(placa, modelo, capacidad)
                print(f"Vehículo creado. ID: {v.id_vehiculo}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            vehiculos = vehiculo_crud.obtener_todos()
            if not vehiculos:
                print("No hay vehículos registrados.")
            for v in vehiculos:
                print(
                    f"ID: {v.id_vehiculo} | Placa: {v.placa} | Modelo: {v.modelo} | Capacidad: {v.capacidad}"
                )

        elif opcion == "3":
            id_str = input("ID del vehículo a editar: ")
            try:
                id_vehiculo = UUID(id_str)
                placa = input("Nueva placa (Enter para omitir): ") or None
                modelo = input("Nuevo modelo (Enter para omitir): ") or None
                capacidad_str = input("Nueva capacidad (Enter para omitir): ") or None
                capacidad = int(capacidad_str) if capacidad_str else None
                v = vehiculo_crud.actualizar(
                    id_vehiculo, placa=placa, modelo=modelo, capacidad=capacidad
                )
                if v:
                    print(f"Vehículo actualizado: {v.placa}")
                else:
                    print("Vehículo no encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcion == "4":
            id_str = input("ID del vehículo a eliminar: ")
            try:
                id_vehiculo = UUID(id_str)
                ok = vehiculo_crud.eliminar(id_vehiculo)
                print("Vehículo eliminado." if ok else "Vehículo no encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcion == "0":
            break
        else:
            print("Opción no válida.")


def menu_rutas():
    while True:
        print("\n--- RUTAS ---")
        print("1. Crear ruta")
        print("2. Listar rutas")
        print("3. Editar ruta")
        print("4. Eliminar ruta")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Código de la ruta: ")
            nombre = input("Nombre (Enter para omitir): ") or None
            id_usuario_str = input("ID del usuario creador: ")
            try:
                id_usuario = UUID(id_usuario_str)
                r = ruta_crud.crear(codigo, id_usuario, nombre)
                print(f"Ruta creada. ID: {r.id_ruta}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            rutas = ruta_crud.obtener_todos()
            if not rutas:
                print("No hay rutas registradas.")
            for r in rutas:
                print(
                    f"ID: {r.id_ruta} | Código: {r.codigo} | Nombre: {r.nombre} | Activo: {r.activo}"
                )

        elif opcion == "3":
            id_str = input("ID de la ruta a editar: ")
            try:
                id_ruta = UUID(id_str)
                id_editor_str = input("ID del usuario que edita: ")
                id_usuario_edita = UUID(id_editor_str)
                codigo = input("Nuevo código (Enter para omitir): ") or None
                nombre = input("Nuevo nombre (Enter para omitir): ") or None
                activo_str = (
                    input("¿Activo? (s/n, Enter para omitir): ").lower() or None
                )
                activo = activo_str == "s" if activo_str else None
                r = ruta_crud.actualizar(
                    id_ruta,
                    id_usuario_edita,
                    codigo=codigo,
                    nombre=nombre,
                    activo=activo,
                )
                if r:
                    print(f"Ruta actualizada: {r.codigo}")
                else:
                    print("Ruta no encontrada.")
            except ValueError:
                print("ID inválido.")

        elif opcion == "4":
            id_str = input("ID de la ruta a eliminar: ")
            try:
                id_ruta = UUID(id_str)
                ok = ruta_crud.eliminar(id_ruta)
                print("Ruta eliminada." if ok else "Ruta no encontrada.")
            except ValueError:
                print("ID inválido.")

        elif opcion == "0":
            break
        else:
            print("Opción no válida.")


def menu_viajes():
    while True:
        print("\n--- VIAJES ---")
        print("1. Crear viaje")
        print("2. Listar viajes")
        print("3. Editar viaje")
        print("4. Eliminar viaje")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_ruta_str = input("ID de la ruta: ")
                id_ruta = UUID(id_ruta_str)
                id_vehiculo_str = input("ID del vehículo: ")
                id_vehiculo = UUID(id_vehiculo_str)
                id_estacion_origen_str = input("ID estación de origen: ")
                id_estacion_origen = UUID(id_estacion_origen_str)
                id_estacion_destino_str = input("ID estación de destino: ")
                id_estacion_destino = UUID(id_estacion_destino_str)
                fecha_hora_str = input("Fecha y hora de salida (YYYY-MM-DD HH:MM:SS): ")
                fecha_hora_salida = datetime.strptime(
                    fecha_hora_str, "%Y-%m-%d %H:%M:%S"
                )
                id_usuario_str = input("ID del usuario creador: ")
                id_usuario = UUID(id_usuario_str)
                v = viaje_crud.crear(
                    id_ruta,
                    id_vehiculo,
                    id_estacion_origen,
                    id_estacion_destino,
                    fecha_hora_salida,
                    id_usuario,
                )
                print(f"Viaje creado. ID: {v.id_viaje}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            viajes = viaje_crud.obtener_todos()
            if not viajes:
                print("No hay viajes registrados.")
            for v in viajes:
                print(
                    f"ID: {v.id_viaje} | Ruta: {v.id_ruta} | Vehículo: {v.id_vehiculo} | Salida: {v.fecha_hora_salida}"
                )

        elif opcion == "3":
            id_str = input("ID del viaje a editar: ")
            try:
                id_viaje = UUID(id_str)
                id_editor_str = input("ID del usuario que edita: ")
                id_usuario_edita = UUID(id_editor_str)

                id_ruta_str = input("Nuevo ID de ruta (Enter para omitir): ") or None
                id_ruta = UUID(id_ruta_str) if id_ruta_str else None

                id_vehiculo_str = (
                    input("Nuevo ID vehículo (Enter para omitir): ") or None
                )
                id_vehiculo = UUID(id_vehiculo_str) if id_vehiculo_str else None

                id_estacion_origen_str = (
                    input("Nuevo ID estación origen (Enter para omitir): ") or None
                )
                id_estacion_origen = (
                    UUID(id_estacion_origen_str) if id_estacion_origen_str else None
                )

                id_estacion_destino_str = (
                    input("Nuevo ID estación destino (Enter para omitir): ") or None
                )
                id_estacion_destino = (
                    UUID(id_estacion_destino_str) if id_estacion_destino_str else None
                )

                fecha_hora_str = (
                    input(
                        "Nueva fecha y hora (YYYY-MM-DD HH:MM:SS, Enter para omitir): "
                    )
                    or None
                )
                fecha_hora_salida = (
                    datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M:%S")
                    if fecha_hora_str
                    else None
                )

                v = viaje_crud.actualizar(
                    id_viaje,
                    id_usuario_edita,
                    id_ruta=id_ruta,
                    id_vehiculo=id_vehiculo,
                    id_estacion_origen=id_estacion_origen,
                    id_estacion_destino=id_estacion_destino,
                    fecha_hora_salida=fecha_hora_salida,
                )
                if v:
                    print(f"Viaje actualizado. ID: {v.id_viaje}")
                else:
                    print("Viaje no encontrado.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "4":
            id_str = input("ID del viaje a eliminar: ")
            try:
                id_viaje = UUID(id_str)
                ok = viaje_crud.eliminar(id_viaje)
                print("Viaje eliminado." if ok else "Viaje no encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcion == "0":
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu_principal()
