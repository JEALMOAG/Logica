"""
created on 22 Abril 20:56:08 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código implementa un planificador de orden parcial utilizando grafos dirigidos.
Se define una clase PartialOrderPlanner que permite agregar restricciones de
orden entre tareas y luego planificar las tareas de acuerdo con esas
restricciones. Se añaden las tareas al grafo según las restricciones de orden,
y se utiliza un algoritmo para encontrar un plan que cumpla con esas restricciones,
devolviendo una secuencia de tareas planificadas. Si no se puede encontrar un
plan que satisfaga todas las restricciones, devuelve None. Finalmente, se
muestra el plan encontrado o un mensaje indicando que no se encontró un plan.
"""
import networkx as nx  # Importar la biblioteca NetworkX para trabajar con grafos

def planificador_grafico(estado_inicial, estado_final, tareas):
    # Crear un grafo dirigido
    G = nx.DiGraph()  # Creamos un grafo dirigido utilizando la clase DiGraph de NetworkX

    # Añadir nodos para el estado inicial y objetivo
    G.add_node('inicial', tipo='estado')  # Añadimos un nodo para representar el estado inicial con un atributo 'tipo'
    G.add_node('objetivo', tipo='estado')  # Añadimos un nodo para representar el estado objetivo con un atributo 'tipo'

    # Añadir nodos para las acciones
    for tarea in tareas:  # Recorremos todas las tareas disponibles
        G.add_node(tarea, tipo='tarea')  # Añadimos un nodo para cada tarea con un atributo 'tipo'

    # Añadir arcos desde el estado inicial a las acciones aplicables
    for tarea in tareas:  # Recorremos todas las tareas disponibles
        if all(pre in estado_inicial for pre in tareas[tarea]['precondiciones']):  # Verificamos si todas las precondiciones de la acción están en el estado inicial
            G.add_edge('inicial', tarea)  # Añadimos un arco desde el estado inicial hacia la acción

    # Añadir arcos desde las acciones a los estados resultantes
    for tarea in tareas:  # Recorremos todas las tareas disponibles
        for efecto in tareas[tarea]['efectos']:  # Recorremos todos los efectos de la acción
            G.add_edge(tarea, efecto)  # Añadimos un arco desde la acción hacia el estado resultante

    # Añadir arcos desde los estados resultantes al objetivo
    for estado in estado_final:  # Recorremos todos los estados objetivo
        G.add_edge(estado, 'objetivo')  # Añadimos un arco desde el estado resultante hacia el estado objetivo

    # Encontrar el plan
    try:
        return nx.shortest_path(G, source='inicial', target='objetivo')  # Encontramos el camino más corto desde el estado inicial al estado objetivo en el grafo
    except nx.NetworkXNoPath:
        return None  # Si no se encuentra un camino, devolvemos None

# Definir el problema de planificación
estado_inicial = ['En(A)', 'Libre(A)', 'Libre(B)', 'ManoVacia']  # Definimos el estado inicial del problema
estado_objetivo = ['Sobre(A, B)', 'Libre(A)', 'ManoVacia']  # Definimos el estado objetivo del problema
tareas = {  # Definimos las tareas disponibles y sus precondiciones y efectos
    'Recoger(A)': {
        'precondiciones': ['En(A)', 'Libre(A)', 'ManoVacia'],
        'efectos': ['Sosteniendo(A)', 'Libre(A)', 'ManoVacia']
    },
    'Soltar(A)': {
        'precondiciones': ['Sosteniendo(A)'],
        'efectos': ['En(A)', 'Libre(B)', 'ManoVacia']
    },
    'Apilar(A, B)': {
        'precondiciones': ['Sosteniendo(A)', 'Libre(B)'],
        'efectos': ['Sobre(A, B)', 'Libre(A)', 'ManoVacia']
    },
    'Desapilar(A, B)': {
        'precondiciones': ['Sobre(A, B)', 'Libre(A)', 'ManoVacia'],
        'efectos': ['Sosteniendo(A)', 'Libre(B)']
    }
}

# Resolver el problema de planificación
plan = planificador_grafico(estado_inicial, estado_objetivo, tareas)  # Resolvemos el problema de planificación utilizando el algoritmo GRAPHPLAN

# Imprimir el plan
if plan:
    print("Plan encontrado:")  # Imprimimos un mensaje indicando que se encontró un plan
    for paso in plan[1:]:  # Recorremos el plan omitiendo el primer paso (estado inicial)
        print(paso)  # Imprimimos cada paso del plan
else:
    print("No se encontró un plan.")  # Imprimimos un mensaje indicando que no se encontró un plan





