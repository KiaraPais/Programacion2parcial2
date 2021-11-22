ejercicio_Uno = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

class EjercicioUno:
    """Se va a utilizar esta clase para resolver el ejercicio 1""" 

    def cantidad_aparece(self):
        """Cuenta la cantidad de veces que aparecen las palabras en un texto"""

        try:
            listaPalabras = ejercicio_Uno.split()
    
            frecuenciaPalabra = []
            for l in listaPalabras:
                frecuenciaPalabra.append(listaPalabras.count(l))

            print(str(list(zip(listaPalabras, frecuenciaPalabra)))) 
        except:
            print("Surgio un error al contar la cantidad de veces que aparecen las palabras")
    

    def longitud_palabra(self):
        "Devuelve la longitud de la palabra"

        try:
            listaPalabras = ejercicio_Uno.split()
    
            longitudPalabra = []
            for l in listaPalabras:
                longitudPalabra.append(len(l))

            print(str(dict(zip(listaPalabras, longitudPalabra))))
        except:
            print("Surgio un error al devolver la longitud de la palabra")