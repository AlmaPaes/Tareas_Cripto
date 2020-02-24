"""
Ejercicio 3
Sustituye los caracteres presentes en un texto con otros caracteres
Autores: Páes Alcalá Alma Rosa y Valderrama Silva Alejandro Tonatiuh
Fecha: Febrero 2020
"""

#Sustituciones de caracteres
midiccionario = {
    'M' : 'Q',
    'Y' : 'U', 
    'G' : 'E', 
    'Q' : 'L', 
    'N' : 'D', 
    'K' : 'Y', 
    'D' : 'M', 
    'R' : 'A', 
    'I' : 'R', 
    'P' : 'H', 
    'J' : 'O', 
    'A' : 'N', 
    'B' : 'I', 
    'S' : 'G', 
    'H' : 'S', 
    'C' : 'B', 
    'L' : 'T', 
    'T' : 'C', 
    'Ñ' : 'P', 
    'O' : 'V', 
    'V' : 'J', 
    'W' : 'F', 
    'E' : 'Z', 
    'U' : 'X', 
    'X' : 'W', 
    'Z' : 'Ñ', 
    'F' : 'K'
}

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
inputFile = dir_path + "/texto.enc"
outputFile = dir_path + "/limpio.txt"

if not os.path.exists(outputFile):
    with open(outputFile, 'w'): pass

with open(inputFile, "r") as entrada:
    with open(outputFile, "w") as salida:
        while True:
            data = entrada.read(1)
            if data == '':
                break
            if data not in midiccionario:
                salida.write(data)
            else:
                salida.write(midiccionario[data])
        entrada.close()
        salida.close()