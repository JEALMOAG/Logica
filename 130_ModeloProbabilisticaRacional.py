"""
created on 22 Abril 07:23:28 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código implementa una clase llamada RedBayesiana que representa una red
bayesiana y proporciona métodos para agregar nodos y calcular probabilidades
condicionales. Cada nodo tiene padres y una tabla de probabilidades
condicionales. Se crean instancias de la clase, se agregan nodos y relaciones
entre ellos, y luego se realizan consultas de probabilidad basadas en la
evidencia proporcionada. El código demuestra cómo usar la red bayesiana para
calcular la probabilidad de eventos dados ciertos valores de evidencia.
"""
class RedBayesiana:  # Define una clase llamada RedBayesiana
    def __init__(self):  # Define el método de inicialización de la clase
        self.nodos = {}  # Diccionario para almacenar los nodos de la red

    def agregar_nodo(self, nombre_nodo, padres, probabilidades):  # Define un método para agregar un nodo a la red
        self.nodos[nombre_nodo] = {'padres': padres, 'probabilidades': probabilidades}  # Agrega un nodo a la red con sus padres y probabilidades

    def calcular_probabilidad(self, nombre_nodo, evidencia):  # Define un método para calcular la probabilidad de un nodo dado la evidencia
        # Verifica si el nodo está presente en la red
        if nombre_nodo not in self.nodos:
            print(f"El nodo {nombre_nodo} no está presente en la red.")
            return None

        nodo = self.nodos[nombre_nodo]
        padres = nodo['padres']
        probabilidades = nodo['probabilidades']

        # Verifica si se proporciona evidencia para todos los padres del nodo
        if set(padres) != set(evidencia.keys()):
            print(f"No se proporcionó evidencia para todos los padres de {nombre_nodo}.")
            return None

        # Calcula la probabilidad condicional del nodo dados los valores de sus padres
        indice_probabilidad = tuple(evidencia[padre] for padre in padres)
        probabilidad = probabilidades[indice_probabilidad]

        return probabilidad

# Creamos una red bayesiana
rb = RedBayesiana()

# Añadimos los nodos y sus relaciones
rb.agregar_nodo('Lluvia', [], {(): 0.2})  # Nodo raíz con probabilidad marginal de lluvia
rb.agregar_nodo('Riego', ['Lluvia'], {(True,): 0.1, (False,): 0.5})  # Nodo de riego condicionado a la lluvia

# Realizamos algunas consultas de probabilidad
print("Probabilidad de lluvia:")
print("P(Lluvia) =", rb.calcular_probabilidad('Lluvia', {}))

print("\nProbabilidad de riego dado que está lloviendo:")
print("P(Riego | Lluvia=True) =", rb.calcular_probabilidad('Riego', {'Lluvia': True}))

print("\nProbabilidad de riego dado que no está lloviendo:")
print("P(Riego | Lluvia=False) =", rb.calcular_probabilidad('Riego', {'Lluvia': False}))



