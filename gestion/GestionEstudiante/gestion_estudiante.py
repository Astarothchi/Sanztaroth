import json
import os
import numpy as np
from GestionCursos.gestion_cursos import *
from GestionCursos.Calificaciones.calificaciones import agregar_calificacion

DATA_FILE = "db_sys/estudiantes.json"
LOG_FILE = "db_sys/eliminaciones.json"

os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

estudiantes = []

def cargar_datos():
    global estudiantes
    try:
        with open(DATA_FILE, 'r') as file:
            estudiantes = json.load(file)
            for est in estudiantes:
                # Convertir datos_fijos a tupla
                est["datos_fijos"] = tuple(est["datos_fijos"])
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

def registrar_estudiante():
    try:
        nombre = input("Ingrese el nombre del estudiante: ")
        matricula = int(input("Ingrese el número de matrícula: "))
        rut = int(input("Ingrese el RUT sin punto y ni guion: "))

        # Mantener datos_fijos como tupla
        datos_fijos = (matricula, nombre)

        estudiante = {
            "datos_fijos": datos_fijos,  
            "rut": rut,
            "cursos": [],  
            "calificaciones": {}  
        }
        estudiantes.append(estudiante)
        guardar_datos()
        print("Estudiante registrado exitosamente.")
    except:
        print("Valor ingresado no válido")


def eliminar_estudiante():
    try:
        matricula = int(input("Ingrese la matrícula del estudiante a eliminar: "))
        for estudiante in estudiantes:
            if estudiante["datos_fijos"][0] == matricula:
                estudiantes.remove(estudiante)
                guardar_datos()
                with open(LOG_FILE, 'a') as log_file:
                    json.dump(estudiante, log_file)
                    log_file.write('\n')
                print("Estudiante eliminado exitosamente.")
                return
        print("Estudiante no encontrado.")
    except:
        print("Valor ingresado no valido")

def actualizar_estudiante():
    try:
        matricula = int(input("Ingrese la matrícula del estudiante a actualizar: "))
        for estudiante in estudiantes:
            if estudiante["datos_fijos"][0] == matricula:
                nuevo_nombre = input("Ingrese el nuevo nombre del estudiante: ")
                nuevo_rut = input("Ingrese el nuevo RUT: ")
                if nuevo_nombre:
                    estudiante["datos_fijos"] = (estudiante["datos_fijos"][0], nuevo_nombre)
                if nuevo_rut:
                    estudiante["rut"] = nuevo_rut

                guardar_datos()
                print("Información del estudiante actualizada exitosamente.")
                return
        print("Estudiante no encontrado.")
    except:
        print("Valor no valido")

def asignar_curso():
    try:
        matricula = int(input("Ingrese la matrícula del estudiante: "))
        for estudiante in estudiantes:
            if estudiante["datos_fijos"][0] == matricula:
                mostrar_cursos()
                curso = input("Ingrese el nombre del curso para asignar: ")
                if curso not in estudiante["cursos"]:
                    estudiante["cursos"].append(curso)
                    estudiante["calificaciones"][curso] = np.array([])  
                    guardar_datos()
                    print(f"Curso {curso} asignado a {estudiante['datos_fijos'][1]}.")
                else:
                    print("El curso ya está asignado al estudiante.")
                return
        print("Estudiante no encontrado.")
    except:
        print("Valor no valido")

def modificar_nota():
    try:
        matricula = int(input("Ingrese la matrícula del estudiante: "))
        for estudiante in estudiantes:
            if estudiante["datos_fijos"][0] == matricula:
                curso = input("Ingrese el nombre del curso de la nota a modificar: ")
                if curso in estudiante["calificaciones"]:
                    notas = estudiante["calificaciones"][curso]
                    print("Calificaciones actuales:", notas)
                    indice = int(input("Ingrese el índice de la nota que desea modificar: "))
                    if 0 <= indice < len(notas):
                        nueva_nota = float(input("Ingrese la nueva nota: "))
                        notas[indice] = nueva_nota
                        guardar_datos()
                        print("Nota modificada exitosamente.")
                    else:
                        print("Índice no válido.")
                else:
                    print("El curso no tiene calificaciones registradas.")
                return
        print("Estudiante no encontrado.")
    except:
        print("Valor ingresado no valido")

def eliminar_nota():
    try:
        matricula = int(input("Ingrese la matrícula del estudiante: "))
        for estudiante in estudiantes:
            if estudiante["datos_fijos"][0] == matricula:
                curso = input("Ingrese el nombre del curso de la nota a eliminar: ")
                if curso in estudiante["calificaciones"]:
                    notas = estudiante["calificaciones"][curso]
                    print("Calificaciones actuales:", notas)
                    indice = int(input("Ingrese el índice de la nota que desea eliminar: "))
                    if 0 <= indice < len(notas):
                        estudiante["calificaciones"][curso] = np.delete(notas, indice)
                        guardar_datos()
                        print("Nota eliminada exitosamente.")
                    else:
                        print("Índice no válido.")
                else:
                    print("El curso no tiene calificaciones registradas.")
                return
        print("Estudiante no encontrado.")
    except:
        print("Valor ingresado no valido")

def modificar_curso():
    try:
        matricula = int(input("Ingrese la matrícula del estudiante: "))
        for estudiante in estudiantes:
            if estudiante["datos_fijos"][0] == matricula:
                curso_actual = input("Ingrese el curso que desea modificar: ")
                if curso_actual in estudiante["cursos"]:
                    nuevo_curso = input("Ingrese el nuevo nombre del curso: ")
                    estudiante["cursos"].remove(curso_actual)
                    estudiante["cursos"].append(nuevo_curso)
                    estudiante["calificaciones"][nuevo_curso] = estudiante["calificaciones"].pop(curso_actual)
                    guardar_datos()
                    print("Curso modificado exitosamente.")
                else:
                    print("El curso no está asignado al estudiante.")
                return
        print("Estudiante no encontrado.")
    except:
        print("Valor ingresado no valido")

def eliminar_curso():
    try:
        matricula = int(input("Ingrese la matrícula del estudiante: "))
        for estudiante in estudiantes:
            if estudiante["datos_fijos"][0] == matricula:
                curso = input("Ingrese el curso que desea eliminar: ")
                if curso in estudiante["cursos"]:
                    estudiante["cursos"].remove(curso)
                    estudiante["calificaciones"].pop(curso, None)
                    guardar_datos()
                    print("Curso eliminado exitosamente.")
                else:
                    print("El curso no está asignado al estudiante.")
                return
        print("Estudiante no encontrado.")
    except:
        print("Valor ingresado no valido")

def ver_estudiantes():
    cargar_datos()
    
    if not estudiantes:
        print("No hay estudiantes registrados")
        return
    print("\n--- Lista de Estudiantes ---")
    
    estudiantes_array = np.array(estudiantes, dtype=object)
    
    for estudiante in estudiantes_array:
        print(f"Rut: {estudiante['rut']}, Nombre: {estudiante['datos_fijos'][1]}")
        cursos = estudiante.get("cursos", [])
        if cursos:
            print("  Cursos inscritos: ")
            for curso in cursos:
                print (f"    - {curso}")
        else:
            print ("   No tiene cursos inscritos")
        calificaciones = estudiante.get("calificaciones", {})
        
        if calificaciones:
            print("  Calificaciones")
            for curso, calificacion in calificaciones.items():
                print (f"  {curso}:{calificacion}")
        else:
            print ("  No tiene Calificaciones registradas")

def menu_estudiante():
    while True:
        print("\n--- Gestión de Estudiantes ---")
        print("1. Registrar Estudiante")
        print("2. Eliminar Estudiante")
        print("3. Ver Estudiantes")
        print("4. Actualizar Estudiante")
        print("5. Asignar Curso a Estudiante")
        print("6. Agregar Calificación a Estudiante")
        print("7. Modificar Nota")
        print("8. Eliminar Nota")
        print("9. Modificar Curso")
        print("10. Eliminar Curso")
        print("11. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            eliminar_estudiante()
        elif opcion == "3":
            ver_estudiantes()
        elif opcion == "4":
            actualizar_estudiante()
        elif opcion == "5":
            asignar_curso()
        elif opcion == "6":
            agregar_calificacion()
        elif opcion == "7":
            modificar_nota()
        elif opcion == "8":
            eliminar_nota()
        elif opcion == "9":
            modificar_curso()
        elif opcion == "10":
            eliminar_curso()
        elif opcion == "11":
            break
        else:
            print("Opción no válida. Intente de nuevo.")