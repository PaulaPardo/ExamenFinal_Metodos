# Ejercicio 2
# Complete el siguiente codigo para recorrer la lista `x` e imprima
# los numeros impares y que pare de imprimir al encontrar un numero mayor a 800
import numpy as np

x = np.int_(np.random.random(100)*1000)
lista = []

for i in x:
    if(i%2 != 0):
        if(i<802):
            lista.append(i)      
print(lista)



