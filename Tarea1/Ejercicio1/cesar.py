"""
Ejercicio 1, incisos a y b
Implementación del método de César, donde se prueban todas las llaves posibles
para encontrar un mensaje legible
Autores: Páes Alcalá Alma Rosa y Valderrama Silva Alejandro Tonatiuh
Fecha: Febrero 2020
"""

NUM_ALFABETO = 26
mensaje1 = list("SLYDPYQCGLQNGPYBMPY")
mensaje2 = list("CVVCEMVJGKORNGOGPVCVKQP")

#Mensaje a descifrar
mensaje = mensaje1

for k in range(0,NUM_ALFABETO):
	print("Llave: " + str(k))
	claro = []
	for m in mensaje:
		num = ord(m)
		num = num - 65
		num = num - k
		modulo = num % NUM_ALFABETO
		newNumber = modulo + 65
		claro.append(chr(newNumber))
	print(claro)