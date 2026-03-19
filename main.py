"""
Módulo principal del Sistema de Transporte Público.
Menú interactivo para gestionar Usuarios y Tarjetas con persistencia en Neon.
"""

from src.crud import usuario_crud, tarjeta_crud
from uuid import UUID


def menu_principal():
    while True:
        print("\n===== SISTEMA DE TRANSPORTE PÚBLICO =====")
        print("1. Gestión de Usuarios")
        print("2. Gestión de Tarjetas")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_usuarios()
        elif opcion == "2":
            menu_tarjetas()
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
                print(f"ID: {u.id_usuario} | Usuario: {u.nombre_usuario} | Rol: {u.rol} | Activo: {u.activo}")

        elif opcion == "3":
            id_str = input("ID del usuario a editar: ")
            try:
                id_usuario = UUID(id_str)
                nombre = input("Nuevo nombre de usuario (Enter para omitir): ") or None
                contrasena = input("Nueva contraseña (Enter para omitir): ") or None
                rol = input("Nuevo rol (Enter para omitir): ") or None
                u = usuario_crud.actualizar(id_usuario, nombre_usuario=nombre, contrasena=contrasena, rol=rol)
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
                t = tarjeta_crud.crear(saldo=saldo, id_usuario=id_usuario, id_usuario_creacion=id_usuario)
                print(f"Tarjeta creada. ID: {t.id_tarjeta}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            tarjetas = tarjeta_crud.obtener_todos()
            if not tarjetas:
                print("No hay tarjetas registradas.")
            for t in tarjetas:
                print(f"ID: {t.id_tarjeta} | Saldo: {t.saldo} | Tipo: {t.tipo} | Activo: {t.activo} | Usuario: {t.id_usuario}")

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


if __name__ == "__main__":
    menu_principal()
