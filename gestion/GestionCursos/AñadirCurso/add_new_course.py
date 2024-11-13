from GestionCursos.gestion_cursos import *

import numpy as np
import json
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
        
def agregar_curso(cursos):
    nuevo_curso = input("Ingrese el nombre del nuevo curso: ")
    if nuevo_curso and nuevo_curso not in cursos:
        cursos.append(nuevo_curso)
        print(f"Curso {nuevo_curso} agregado.")
    else:
        print("Curso ya existe o nombre inválido.")