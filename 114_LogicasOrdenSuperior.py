"""
Created on 18 April  06:09:39 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
Este código implementa funciones de lógica de orden superior (AND, OR, NOT, IMPLIES, EQUIV)
 utilizando la función `reduce` de la biblioteca `functools` en Python. 
 Estas funciones permiten realizar operaciones lógicas entre múltiples valores
 de entrada de manera más flexible. Luego, se proporciona un ejemplo de uso de
 estas funciones con valores de prueba `p`, `q`, y `r`, y se imprimen los 
 resultados esperados para cada operación lógica.
'''

from functools import reduce

# Definición de funciones de lógica de orden superior

# Función AND
def AND(*args):
    return reduce(lambda x, y: x and y, args)

# Función OR
def OR(*args):
    return reduce(lambda x, y: x or y, args)

# Función NOT
def NOT(x):
    return not x

# Función IMPLIES
def IMPLIES(x, y):
    return (not x) or y

# Función EQUIV
def EQUIV(x, y):
    return (x and y) or ((not x) and (not y))

# Ejemplo de uso de lógica de orden superior

# Definimos algunos valores de prueba
p = True
q = False
r = True

# Probando las funciones lógicas
print("AND(p, q, r) =", AND(p, q, r))  # Salida esperada: False
print("OR(p, q, r) =", OR(p, q, r))     # Salida esperada: True
print("NOT(p) =", NOT(p))               # Salida esperada: False
print("IMPLIES(p, q) =", IMPLIES(p, q)) # Salida esperada: False
print("EQUIV(p, q) =", EQUIV(p, q))     # Salida esperada: False
