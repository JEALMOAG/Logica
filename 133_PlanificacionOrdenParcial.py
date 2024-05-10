"""
created on 22 Abril 15:34:12 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código implementa un planificador de orden parcial que busca planificar un
conjunto de tareas respetando las restricciones de orden entre ellas. Utiliza
la clase Tarea para representar cada tarea con un nombre y una duración.
La clase PlanificadorOrdenParcial administra las restricciones de orden entre
las tareas y planifica su ejecución. El método planificar genera un plan
secuencial de ejecución de tareas, teniendo en cuenta las restricciones de
orden establecidas. Finalmente, imprime el plan generado, mostrando el nombre
de cada tarea y su duración acumulada.
"""
from collections import defaultdict  # Importar la clase defaultdict para crear diccionarios con valores predeterminados

class Tarea:  # Definir la clase Tarea para representar una tarea
    def __init__(self, nombre, duracion):  # Método para inicializar una tarea con un nombre y una duración
        self.nombre = nombre  # Nombre de la tarea
        self.duracion = duracion  # Duración de la tarea

class PlanificadorOrdenParcial:  # Definir la clase PlanificadorOrdenParcial para el planificador de orden parcial
    def __init__(self):  # Método para inicializar el planificador
        self.restricciones_orden = defaultdict(list)  # Diccionario para almacenar las restricciones de orden entre tareas

    def agregar_restriccion_orden(self, antes, despues):  # Método para añadir una restricción de orden entre dos tareas
        self.restricciones_orden[despues].append(antes)  # Añadir la tarea 'antes' como tarea anterior a la tarea 'despues'

    def planificar(self, tareas):  # Método para planificar las tareas
        planificadas = set()  # Conjunto para almacenar las tareas ya planificadas
        duracion_total = 0  # Inicializar la duración total del plan a 0
        while len(planificadas) < len(tareas):  # Mientras queden tareas por planificar
            for tarea in tareas:  # Para cada tarea en la lista de tareas
                if tarea in planificadas:  # Si la tarea ya está planificada, continuar con la siguiente tarea
                    continue
                if all(pre in planificadas for pre in self.restricciones_orden[tarea]):  # Si todas las tareas previas están planificadas
                    planificadas.add(tarea)  # Planificar la tarea actual
                    duracion_total += tarea.duracion  # Añadir la duración de la tarea actual a la duración total
                    yield tarea, duracion_total  # Devolver la tarea planificada y la duración total

# Crear un planificador de orden parcial
planificador = PlanificadorOrdenParcial()

# Definir las tareas y las restricciones de orden entre ellas
tarea_A = Tarea('A', 2)
tarea_B = Tarea('B', 3)
tarea_C = Tarea('C', 4)
tarea_D = Tarea('D', 2)
tarea_E = Tarea('E', 3)

planificador.agregar_restriccion_orden(tarea_A, tarea_B)
planificador.agregar_restriccion_orden(tarea_B, tarea_C)
planificador.agregar_restriccion_orden(tarea_C, tarea_D)
planificador.agregar_restriccion_orden(tarea_C, tarea_E)

# Planificar las tareas
tareas = [tarea_A, tarea_B, tarea_C, tarea_D, tarea_E]
plan = planificador.planificar(tareas)

# Imprimir el plan
print("El plan es:")
for tarea, duracion_total in plan:  # Para cada tarea y su duración total en el plan
    print(f"Tarea: {tarea.nombre}, Duración acumulada: {duracion_total}")  # Imprimir el nombre de la tarea y su duración acumulada
