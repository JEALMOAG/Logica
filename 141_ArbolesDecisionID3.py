"""
created on 24 Abril 07:54:12 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código proporciona una implementación del algoritmo ID3 para construir un
árbol de decisión y predecir la etiqueta de nuevos ejemplos. Utiliza conceptos
como entropía y ganancia de información para determinar qué atributo dividir.
Primero, define una clase Nodo para representar nodos en el árbol de decisión.
Luego, incluye funciones para calcular la entropía de un conjunto de datos,
dividir los datos según un atributo dado, encontrar el mejor atributo para
dividir y construir el árbol de decisión recursivamente. Finalmente, utiliza
el árbol construido para predecir la etiqueta de nuevos ejemplos. El código
está organizado en funciones que realizan tareas específicas para mantener una
estructura clara y modular.
"""
import math  # Importa el módulo math para utilizar funciones matemáticas

# Definición de la clase Nodo para el árbol de decisión
class Nodo:  # Define una clase llamada Nodo
    def __init__(self, valor):  # Define el método de inicialización de la clase Nodo con el atributo valor
        self.valor = valor  # Asigna el valor al atributo valor
        self.hijos = {}  # Inicializa un diccionario vacío para almacenar los hijos del nodo

# Función para calcular la entropía de un conjunto de datos
def calcular_entropia(datos):  # Define una función llamada calcular_entropia que toma un conjunto de datos como entrada
    etiquetas = {}  # Inicializa un diccionario vacío para contar las etiquetas únicas en el conjunto de datos
    for item in datos:  # Itera sobre cada elemento (instancia) en el conjunto de datos
        etiqueta = item[-1]  # Obtiene la etiqueta del elemento
        if etiqueta not in etiquetas:  # Verifica si la etiqueta no está en el diccionario
            etiquetas[etiqueta] = 0  # Agrega la etiqueta al diccionario y establece su conteo en cero
        etiquetas[etiqueta] += 1  # Incrementa el conteo de la etiqueta en uno

    entropia = 0.0  # Inicializa la entropía en cero
    for etiqueta in etiquetas:  # Itera sobre cada etiqueta en el diccionario de etiquetas
        probabilidad = etiquetas[etiqueta] / len(datos)  # Calcula la probabilidad de la etiqueta
        entropia -= probabilidad * math.log2(probabilidad)  # Calcula la contribución de esta etiqueta a la entropía total

    return entropia  # Retorna la entropía calculada

# Función para dividir el conjunto de datos en subconjuntos basados en un atributo dado
def dividir_datos(datos, indice_atributo):  # Define una función llamada dividir_datos que toma un conjunto de datos y un índice de atributo como entrada
    datos_divididos = {}  # Inicializa un diccionario vacío para almacenar los subconjuntos de datos divididos por los valores del atributo
    for item in datos:  # Itera sobre cada elemento (instancia) en el conjunto de datos
        valor_atributo = item[indice_atributo]  # Obtiene el valor del atributo en el índice dado
        if valor_atributo not in datos_divididos:  # Verifica si el valor del atributo no está en el diccionario
            datos_divididos[valor_atributo] = []  # Agrega el valor del atributo al diccionario y establece su lista de elementos en vacío
        datos_divididos[valor_atributo].append(item)  # Agrega el elemento al subconjunto correspondiente basado en el valor del atributo
    return datos_divididos  # Retorna el diccionario de datos divididos

# Función para encontrar el atributo con la mayor ganancia de información
def encontrar_mejor_atributo(datos, atributos):  # Define una función llamada encontrar_mejor_atributo que toma un conjunto de datos y una lista de atributos como entrada
    entropia_inicial = calcular_entropia(datos)  # Calcula la entropía inicial del conjunto de datos
    mejor_ganancia_info = 0.0  # Inicializa la mejor ganancia de información en cero
    mejor_atributo = None  # Inicializa el mejor atributo como None
    for i in range(len(atributos)):  # Itera sobre cada índice de atributo en la lista de atributos
        valores_atributo = set([item[i] for item in datos])  # Obtiene los valores únicos del atributo en el índice dado
        entropia_nueva = 0.0  # Inicializa la entropía después de dividir por este atributo en cero
        for valor in valores_atributo:  # Itera sobre cada valor del atributo
            datos_divididos = dividir_datos(datos, i)  # Divide el conjunto de datos por el valor del atributo
            probabilidad = len(datos_divididos[valor]) / len(datos)  # Calcula la probabilidad de este valor del atributo
            entropia_nueva += probabilidad * calcular_entropia(datos_divididos[valor])  # Calcula la entropía después de dividir por este valor del atributo
        ganancia_info = entropia_inicial - entropia_nueva  # Calcula la ganancia de información al dividir por este atributo
        if ganancia_info > mejor_ganancia_info:  # Verifica si la ganancia de información es mayor que la mejor ganancia de información encontrada hasta ahora
            mejor_ganancia_info = ganancia_info  # Actualiza la mejor ganancia de información
            mejor_atributo = i  # Actualiza el mejor atributo con este índice
    return mejor_atributo  # Retorna el índice del mejor atributo encontrado

# Función para construir el árbol de decisión usando el algoritmo ID3
def construir_arbol_decision(datos, atributos, etiquetas):  # Define una función llamada construir_arbol_decision que toma un conjunto de datos, una lista de atributos y una lista de etiquetas como entrada
    # Caso base: si todos los ejemplos tienen la misma etiqueta, devolver un nodo hoja con esa etiqueta
    etiquetas_datos = [item[-1] for item in datos]  # Obtiene las etiquetas de los ejemplos
    if len(set(etiquetas_datos)) == 1:  # Verifica si todas las etiquetas son iguales
        return Nodo(etiquetas_datos[0])  # Retorna un nodo hoja con la etiqueta única encontrada

    # Si no quedan atributos, devolver un nodo hoja con la etiqueta más común
    if len(atributos) == 0:  # Verifica si no quedan atributos para dividir
        etiqueta_mas_comun = max(set(etiquetas_datos), key=etiquetas_datos.count)  # Encuentra la etiqueta más común en los ejemplos
        return Nodo(etiqueta_mas_comun)  # Retorna un nodo hoja con la etiqueta más común encontrada

    # Encontrar el mejor atributo para dividir
    mejor_atributo_indice = encontrar_mejor_atributo(datos, atributos)  # Encuentra el índice del mejor atributo
