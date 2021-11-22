import re

secuencia_adn = "TGCCACAAATGTGACAGGACGCCGATGGGTACCGGACTTTAGGTCGAGCACAGTTCGGTAACGGAGAGACCCTGCGGCGTACTTCATTATGTATATGGAACGTGCCCAAGTGACGCCAGGCAAGTCTCAGCTGGTTCCTGTGTTAGCTCGAGGGTAGACATACGAGCTGATTGAACATGGGTTGGGGGCCTCGAACCGTCGAGGACCCCATAGTACCTCGGAGACCAAGTAGGGCAGCCTATAGTTTGAAGCAGAACTATTTCGGGGGGCGAGCCCTCATCGTCTCTTCTGCGGATGACTCAACACGCTAGGGACGTGAAGTCGATTCCTTCGATGGTTATAAATCAAAGACCGAGGACCGCAAGGTGCGGCGGTGCACAAGCAATTGACAACTAACCACCGTGTATTCATTATGGTACCAGGAACTTTAAGCCGAGTCAATGAAGCTCGCATTACAGTGTTTACCGCATCTTGCCGTTACT"

class EjercicioDos:
    """Se va a utilizar esta clase para resolver el ejercicio 2"""

    def cantidad_aparece_CATT(self):
        """Encuentra la cantidad de veces que aparece la serie CATT en el texto"""

        try:
            #findall: devuelve una lista con las ocurrencia de la palabra. 
            matched_times = len(re.findall('CATT', secuencia_adn))
            print(matched_times)
        except:
            print("Surgio un error en la busqueda de CATT")

    def probar_existencia(self):
        """Probar que existe la serie CAAAGACCGAGGACC"""
        try:
            if re.search("CAAAGACCGAGGACC", secuencia_adn):
                print("Existe")
            else:
                print("No existe")
        except:
            print("Surgio un error en la busqueda de CAAAGACCGAGGACC")

    def probar_no_existencia(self):
        """Probar que NO existe la serie TTGAACCAA"""
        try:
            if re.search("TTGAACCAA", secuencia_adn):
                print("Existe")
            else:
                print("No existe")
        except:
            print("Surgio un error en la busqueda de TTGAACCAA")