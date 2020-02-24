"""
Ejercicio 7, inciso c
Implementación del método afín para descifrar un audio a partir de una llave ya descubierta
Autores: Páes Alcalá Alma Rosa y Valderrama Silva Alejandro Tonatiuh
Fecha: Febrero 2020
"""

import os

def inverse(a, n):
    """
    Encuentra el inverso multiplicativo del numero dado. Esto 
    claro, tomando en cuenta que trabajamos con modulo n. 
    Parámetro:
        a -- el numero al cual se le quiere encontrar el
            inverso multiplicativo.
        n -- el tamanio del alfabeto
    Este algoritmo esta basado en un pseudocodigo de wikipedia:
    https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    """
    
    t, newT = 0, 1
    r, newR = n, a

    while (newR != 0):
        q = r // newR
        t, newT = newT, t - q * newT 
        r, newR = newR, r - q * newR

    if (r != 1): 
        return None #No tiene inverso multiplicativo
    if (t < 0):
        t = t + n

    return t


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    inputFile = dir_path + "/audio.enc"
    outputFile = dir_path + "/audio.mp3"

    if not os.path.exists(outputFile):
        with open(outputFile, 'w'): pass

    #Conocemos la longitud en bytes del archivo de entrada
    longitud = os.path.getsize(inputFile)

    key1 = 13
    key2 = 255
    NUM_ALFABETO = 256

    with open(inputFile, "rb") as entrada:
        with open(outputFile, "wb") as salida:
            while longitud > 0:
                data = entrada.read(1)
                if data != b'':
                    numero = ord(data)
                    numero = numero - key2
                    numeroNuevo = numero * inverse(key1,NUM_ALFABETO)
                    numeroNuevo = numeroNuevo % NUM_ALFABETO
                    salida.write(bytes([numeroNuevo]))
                else:
                    salida.write(b'')
                longitud = longitud - 1
            entrada.close()
            salida.close()
