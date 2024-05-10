"""
created on 22 Abril 13:09:23 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código implementa el algoritmo de búsqueda en anchura (BFS) para encontrar
un camino desde un estado inicial hasta un estado objetivo en una cuadrícula.
Define clases para representar estados y problemas de planificación, así como
funciones para realizar la búsqueda y imprimir la solución encontrada.
El algoritmo explora gradualmente todos los estados posibles desde el estado
inicial hasta encontrar el estado objetivo, utilizando una cola para organizar
los estados por explorar.
"""
from collections import deque  # Importar la clase deque para la implementación de la cola

class Estado:
    def __init__(self, x, y):  # Definir la clase Estado para representar un estado en la cuadrícula
        self.x = x  # Coordenada x del estado
        self.y = y  # Coordenada y del estado

    def __eq__(self, other):  # Método para verificar la igualdad de dos estados
        return self.x == other.x and self.y == other.y

    def __hash__(self):  # Método para calcular el hash de un estado (necesario para usarlo en conjuntos)
        return hash((self.x, self.y))

class Problema:
    def __init__(self, estado_inicial, estado_objetivo):  # Definir la clase Problema para representar el problema de planificación
        self.estado_inicial = estado_inicial  # Estado inicial del problema
        self.estado_objetivo = estado_objetivo  # Estado objetivo del problema

    def acciones(self, estado):  # Método para obtener las acciones posibles desde un estado dado
        acciones_posibles = []  # Lista para almacenar las acciones posibles
        acciones_posibles.append(Estado(estado.x + 1, estado.y))  # Mover hacia la derecha
        acciones_posibles.append(Estado(estado.x - 1, estado.y))  # Mover hacia la izquierda
        acciones_posibles.append(Estado(estado.x, estado.y + 1))  # Mover hacia arriba
        acciones_posibles.append(Estado(estado.x, estado.y - 1))  # Mover hacia abajo
        acciones_posibles = [accion for accion in acciones_posibles if 0 <= accion.x < 5 and 0 <= accion.y < 5]  # Filtrar acciones para evitar salir de la cuadrícula
        return acciones_posibles

    def prueba_objetivo(self, estado):  # Método para verificar si un estado es el estado objetivo
        return estado == self.estado_objetivo

def bfs(problema):  # Implementación del algoritmo de búsqueda en anchura
    frontera = deque()  # Declarar la cola para almacenar los estados que deben ser explorados
    explorados = set()  # Declarar el conjunto para almacenar los estados ya explorados
    frontera.append((problema.estado_inicial, []))  # Agregar el estado inicial y una lista vacía para el camino al estado inicial en la cola
    while frontera:  # Mientras haya estados en la cola
        estado_actual, camino = frontera.popleft()  # Obtener el estado actual y el camino actual desde la cola
        if problema.prueba_objetivo(estado_actual):  # Si el estado actual es el estado objetivo
            return camino + [estado_actual]  # Devolver el camino al estado objetivo
        explorados.add(estado_actual)  # Agregar el estado actual a los estados explorados
        for accion in problema.acciones(estado_actual):  # Para cada acción posible desde el estado actual
            if accion not in explorados and (accion, camino + [estado_actual]) not in frontera:  # Si la acción no ha sido explorada ni está en la cola
                frontera.append((accion, camino + [estado_actual]))  # Agregar la acción y el camino actualizado a la cola
    return None  # Devolver None si no se encuentra una solución

def imprimir_solucion(solucion):  # Función para imprimir la solución encontrada
    if solucion is None:  # Si no se encontró una solución
        print("No se encontró una solución.")
    else:  # Si se encontró una solución
        print("La solución encontrada es:")
        for estado in solucion:  # Para cada estado en la solución
            print("({}, {})".format(estado.x, estado.y))  # Imprimir las coordenadas del estado

estado_inicial = Estado(0, 0)  # Definir el estado inicial
estado_objetivo = Estado(4, 4)  # Definir el estado objetivo
problema = Problema(estado_inicial, estado_objetivo)  # Definir el problema de planificación

solucion = bfs(problema)  # Encontrar la solución utilizando BFS
imprimir_solucion(solucion)  # Imprimir la solución encontrada
