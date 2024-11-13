import json
from GestionUniversidad.Datos_Universidad.datos_universidad import *
sedes = ["Concepcion", "Coronel"]

def cargar_sedes():
    """Carga las sedes desde un archivo JSON sin duplicados."""
    try:
        with open("db_sys/sedes.json", "r") as file:
            data = json.load(file)
            for sede in data:
                if sede not in sedes:
                    sedes.append(sede)
    except FileNotFoundError:
        pass


def guardar_sedes():
    """Guarda las sedes en un archivo JSON."""
    with open("db_sys/sedes.json", "w") as file:
        json.dump(sedes, file)

def menu_universidad():
    cargar_sedes()
    while True:
        print("\n--- Gestión de Universidad ---")
        print("1. Ver sedes")
        print("2. Agregar nueva sede")
        print("3. Eliminar sede")
        print("4. Regresar al menú principal")

        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            mostrar_sedes(sedes)

        elif opcion == '2':
            nueva_sede = input("Ingrese el nombre de la nueva sede: ")
            if nueva_sede not in sedes:
                sedes.append(nueva_sede)
                guardar_sedes()
                print("Sede agregada exitosamente.")
            else:
                print("La sede ya existe en el sistema.")

        elif opcion == '3':
            nombre_sede = input("Ingrese el nombre de la sede a eliminar: ")
            if nombre_sede in sedes:
                sedes.remove(nombre_sede)
                guardar_sedes()
                registrar_eliminacion_sede(nombre_sede)
                print("Sede eliminada exitosamente.")
            else:
                print("La sede no se encuentra en el sistema.")

        elif opcion == '4':
            break
        else:
            print("Opción no válida.")

def registrar_eliminacion_sede(sede):
    """Registra la eliminación de una sede en el archivo de eliminaciones."""
    try:
        with open("db_sys/registro_eliminaciones.json", "r") as file:
            eliminaciones = json.load(file)
    except FileNotFoundError:
        eliminaciones = []

    eliminaciones.append({"tipo": "sede", "nombre": sede})
    with open("db_sys/registro_eliminaciones.json", "w") as file:
        json.dump(eliminaciones, file)