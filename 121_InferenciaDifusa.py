"""
Created on 19 April  10:20:17 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
El código implementa un sistema de lógica difusa básico. Utiliza conjuntos 
difusos y reglas difusas para realizar inferencia difusa sobre una entrada dada.
Los conjuntos difusos tienen nombres y funciones de membresía, mientras que 
las reglas difusas relacionan un antecedente y un consecuente. El sistema de
 lógica difusa utiliza estas reglas para realizar inferencia difusa sobre una entrada.
'''
import numpy as np

class ConjuntoDifuso:
    def __init__(self, nombre, funcion_membresia):
        self.nombre = nombre
        self.funcion_membresia = funcion_membresia

    def membresia(self, valor):
        return self.funcion_membresia(valor)


class ReglaDifusa:
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente
        self.consecuente = consecuente

    def activacion(self, entrada):
        return min(self.antecedente.membresia(entrada), self.consecuente.membresia(entrada))


class SistemaDifuso:
    def __init__(self, reglas):
        self.reglas = reglas

    def inferencia(self, entrada):
        resultados = []
        for regla in self.reglas:
            activacion = regla.activacion(entrada)
            resultados.append((regla.consecuente.nombre, activacion))
        return resultados


# Definir funciones de membresía para conjuntos difusos
def triangular(a, b, c):
    def funcion(valor):
        if valor <= a or valor >= c:
            return 0
        elif a < valor <= b:
            return (valor - a) / (b - a)
        elif b < valor < c:
            return (c - valor) / (c - b)
        else:
            return 0
    return funcion


def trapezoidal(a, b, c, d):
    def funcion(valor):
        if valor <= a or valor >= d:
            return 0
        elif a < valor <= b:
            return (valor - a) / (b - a)
        elif c <= valor <= d:
            return 1
        elif b < valor < c:
            return (d - valor) / (d - c)
        else:
            return 0
    return funcion


# Crear conjuntos difusos
temperatura_fria = ConjuntoDifuso("Fria", triangular(0, 0, 10))
temperatura_media = ConjuntoDifuso("Media", triangular(5, 10, 15))
temperatura_caliente = ConjuntoDifuso("Caliente", triangular(10, 20, 20))

# Crear reglas difusas
regla1 = ReglaDifusa(temperatura_fria, temperatura_caliente)
regla2 = ReglaDifusa(temperatura_media, temperatura_media)
regla3 = ReglaDifusa(temperatura_caliente, temperatura_fria)

# Crear sistema difuso
sistema = SistemaDifuso([regla1, regla2, regla3])

# Realizar inferencia difusa
entrada = 12
resultado = sistema.inferencia(entrada)

# Mostrar resultado de la inferencia
print("Resultado de la inferencia:")
for nombre_consecuente, activacion in resultado:
    print(f"{nombre_consecuente}: {activacion}")
