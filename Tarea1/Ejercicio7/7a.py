alphabet = list(range(101))
n = len(alphabet)
key = [99,20]
#a cifrar...
msg = 100
#a descifrar..
c = 23

#Cifrado
m = (key[0]*msg+key[1])%n
print(m)

#Descifrado
def inverse(a, n):
    """
    Encuentra el inverso multiplicativo del numero dado.
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

k_inv = inverse(key[0],n)
#Formula para descifrar un mensaje 
m = (k_inv*(c-key[1]))%n
print(m)

