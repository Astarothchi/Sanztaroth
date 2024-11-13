from GestionCursos.AñadirCurso.add_new_course import agregar_curso
import numpy as np
import json
DATA_FILE = "db_sys/estudiantes.json"
LOG_FILE = "db_sys/eliminaciones.json"

cursos = ["Matematica", "Ingles", "Ciberseguridad", "Modelamiento de datos", "Lenguaje de programacion"]

def cargar_datos():
    global estudiantes
    try:
        with open(DATA_FILE, 'r') as file:
            estudiantes = json.load(file)
            for est in estudiantes:
                for curso, calificaciones in est["calificaciones"].items():
                    est["calificaciones"][curso] = np.array(calificaciones)
    except FileNotFoundError:
        estudiantes = []

def guardar_datos():
    data_to_save = [
        {**est, "calificaciones": {curso: cal.tolist() for curso, cal in est["calificaciones"].items()}}
        for est in estudiantes
    ]
    with open(DATA_FILE, 'w') as file:
        json.dump(data_to_save, file, indent=4)

def mostrar_cursos():
    print("\nCursos disponibles:")
    for curso in cursos:
        print(f"- {curso}")

def actualizar_curso():
    mostrar_cursos()
    curso_viejo = input("Ingrese el nombre del curso que desea actualizar: ")
    if curso_viejo in cursos:
        curso_nuevo = input("Ingrese el nuevo nombre para el curso: ")
        if curso_nuevo and curso_nuevo not in cursos:
            cursos[cursos.index(curso_viejo)] = curso_nuevo
            print("Curso actualizado exitosamente.")
        else:
            print("El nuevo nombre ya existe o es inválido.")
    else:
        print("Curso no encontrado.")
        
def eliminar_curso():
    nombre_curso=input("Ingrese nombre curso: ")
    if nombre_curso in cursos:
        cursos.remove(nombre_curso)
        print(f"Curso '{nombre_curso}' eliminado con éxito.")
    else:
        print(f"El curso '{nombre_curso}' no está registrado.")

def menu_cursos():
    while True:
        print("\n--- Gestión de Cursos ---")
        print("1. Mostrar Cursos")
        print("2. Agregar Curso")
        print("3. Actualizar Curso")
        print("4. Eliminar Curso")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_cursos()
        elif opcion == "2":
            agregar_curso(cursos)
        elif opcion == "3":
            actualizar_curso()
        elif opcion == '4':
            eliminar_curso()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")