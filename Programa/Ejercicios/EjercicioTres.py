from re import A
from Ejercicios.Alumno import Alumno

class EjercicioTres:
    """Se va a utilizar esta clase para resolver el ejercicio 3"""

    def imprimir_Alumnos(self):
        list_alumnos = [Alumno("Pedro", "35", "Doctor", "23.423.532"), Alumno("Juan", "25", "Ingenieria en sistemas", "29.433.532"), Alumno("Kiara", "20", "Bio-Ingenieria", "43.423.232"), Alumno("Azucena", "20", "Doctora", "42.425.532"), Alumno("Angela", "32", "Psicologa", "36.423.902"), Alumno("Estela", "23", "Cocinera", "23.423.523"), Alumno("Martin", "17", "Psicologo", "34.345.345")]

        alumnos = map(lambda a: Alumno(a.__nombre__, str(int(a.__edad__)+1), a.__carrera__, a.__dni__), list_alumnos)

        for alumno in alumnos:
            print(f"Luego de un año el alumno {alumno.__nombre__} tiene {alumno.__edad__} años")