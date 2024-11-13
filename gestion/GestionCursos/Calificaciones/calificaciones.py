import json
import numpy as np


DATA_FILE = "db_sys/estudiantes.json"
LOG_FILE = "db_sys/eliminaciones.json"

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

estudiantes = []
cursos = ["Matematica", "Ingles", "Ciberseguridad", "Modelamiento de datos", "Lenguaje de programacion"]  
sedes = ["Concepcion", "Coronel"]

def agregar_calificacion():
    try: 
        matricula = int(input("Ingrese la matrícula del estudiante: "))
        for estudiante in estudiantes:
            if estudiante["datos_fijos"][0] == matricula:
                if estudiante["cursos"]:
                    print("Cursos inscritos:", ", ".join(estudiante["cursos"]))
                    curso = input("Ingrese el curso para agregar calificación: ")
                    if curso in estudiante["cursos"]:
                        while True:
                            try:
                                calificacion = float(input("Ingrese la calificación (1.0 a 7.0): "))
                                if 1.0 <= calificacion <= 7.0:
                                    if curso not in estudiante["calificaciones"]:
                                        estudiante["calificaciones"][curso] = np.array([])


                                    estudiante["calificaciones"][curso] = np.append(estudiante["calificaciones"][curso], calificacion)
                                    guardar_datos()
                                    print("Calificación agregada exitosamente.")
                                    return
                                else:
                                    print("Calificación fuera de rango. Intente nuevamente.")
                            except ValueError:
                                print("Entrada inválida. Debe ser un número entre 1.0 y 7.0.")
                    else:
                        print("El estudiante no está inscrito en este curso.")
                else:
                    print("El estudiante no está inscrito en ningún curso.")
                return
        print("Estudiante no encontrado.")
    except:
        print("Valor no valido")