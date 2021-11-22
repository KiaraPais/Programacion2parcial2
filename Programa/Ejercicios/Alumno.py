
class Alumno:
    """Clase alumno"""
    __nombre__ = None
    __edad__ = 0
    __carrera__ = None
    __dni__ = None

    def __init__(self, nombre, edad, carrera, dni):
        self.__nombre__ = nombre
        self.__carrera__ = carrera
        self.__edad__ = edad
        self.__dni__ = dni