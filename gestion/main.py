import os
from GestionEstudiante.gestion_estudiante import menu_estudiante
from GestionCursos.gestion_cursos import menu_cursos
from GestionUniversidad.gestion_universidad import menu_universidad

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestión de Estudiantes")
        print("2. Gestión de Cursos")
        print("3. Gestión de Universidad")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_estudiante()
        elif opcion == '2':
            menu_cursos()
        elif opcion == '3':
            menu_universidad()
        elif opcion == '4':
            break
        else:
            print("Opción inválida. Intente de nuevo.")

menu_principal()
