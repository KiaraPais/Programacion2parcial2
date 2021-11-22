from Ejercicios.EjercicioUno import EjercicioUno
from Ejercicios.EjercicioDos import EjercicioDos
from Ejercicios.EjercicioTres import EjercicioTres

if __name__ == '__main__':
    ejercicioUno = EjercicioUno()
    ejercicioDos = EjercicioDos()
    ejercicioTres = EjercicioTres()

    print("1a. Obtiene la cantidad de palabras que hay en una string dada")
    ejercicioUno.cantidad_aparece()

    print("1b. Longitud de cada palabra")
    ejercicioUno.longitud_palabra()

    print("2a. Encontrar l a cantidad de veces que aparece l a serie “CATT”")
    ejercicioDos.cantidad_aparece_CATT()

    print("2b. Probar q ue existe l a serie CAAAGACCGAGGACC")
    ejercicioDos.probar_existencia()

    print("2c. Probar q ue NO existe l a serie TTGAACCAA")
    ejercicioDos.probar_no_existencia()

    print("3. Imprimir lista alumnos")
    ejercicioTres.imprimir_Alumnos()


    