"""
Ejercicio 1, inciso c
Implementación del método de César para descifrar una imagen a partir de una llave ya descubierta
Autores: Páes Alcalá Alma Rosa y Valderrama Silva Alejandro Tonatiuh
Fecha: Febrero 2020
"""

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
inputFile = dir_path + "/imagen.enc"
outputFile = dir_path + "/imagen.jpg"

if not os.path.exists(outputFile):
    with open(outputFile, 'w'): pass

#Conocemos la longitud en bytes del archivo de entrada
longitud = os.path.getsize(inputFile)

cryptoMess = []
key = 101 #Obtenida a mano

with open(inputFile, "rb") as entrada:
    with open(outputFile, "wb") as salida:
        while longitud > 0:
            data = entrada.read(1)
            if data != b'':
                numero = ord(data)
                numero = numero + 256
                numeroNuevo = numero - key
                numeroNuevo = numeroNuevo % 256
                salida.write(bytes([numeroNuevo]))
            else:
                salida.write(b'')
            longitud = longitud - 1
        entrada.close()
        salida.close()




