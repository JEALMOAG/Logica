"""
created on 23 Abril 16:34:15 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código define dos clases: "Agente" y "Entorno". La clase "Agente" representa
un agente con un nombre y una lista de tareas. La clase "Entorno" representa
un entorno que contiene una lista de agentes.
El programa principal crea instancias de agentes, las asigna a un entorno y les
asigna tareas. Luego, imprime las tareas asignadas a cada agente.
"""
class Agente:
    def __init__(self, nombre_agente):
        self.nombre_agente = nombre_agente  # Asigna el nombre del agente
        self.lista_tareas = []  # Inicializa una lista vacía para almacenar las tareas del agente

    def agregar_tarea(self, tarea):
        self.lista_tareas.append(tarea)  # Agrega una tarea a la lista de tareas del agente

    def imprimir_tareas(self):
        print(f"Tareas del agente {self.nombre_agente}:")  # Imprime el encabezado con el nombre del agente
        for i, tarea in enumerate(self.lista_tareas, 1):  # Itera sobre las tareas del agente
            print(f"{i}. {tarea}")  # Imprime el índice y el nombre de cada tarea

class Entorno:
    def __init__(self, lista_agentes):
        self.lista_agentes = lista_agentes  # Inicializa la lista de agentes en el entorno

    def asignar_tarea(self, agente, nombre_tarea):
        if agente in self.lista_agentes:  # Verifica si el agente está presente en el entorno
            agente.agregar_tarea(nombre_tarea)  # Asigna la tarea al agente
            print(f"La tarea '{nombre_tarea}' ha sido asignada al agente '{agente.nombre_agente}'.")  # Imprime un mensaje de confirmación
        else:
            print(f"Error: El agente '{agente.nombre_agente}' no existe en este entorno.")  # Imprime un mensaje de error si el agente no está presente

def main():
    agente_1 = Agente("Agente 1")  # Crea un agente con nombre "Agente 1"
    agente_2 = Agente("Agente 2")  # Crea un agente con nombre "Agente 2"
    agente_3 = Agente("Agente 3")  # Crea un agente con nombre "Agente 3"

    entorno = Entorno([agente_1, agente_2, agente_3])  # Crea un entorno con los agentes especificados

    # Se asignan tareas a los agentes
    entorno.asignar_tarea(agente_1, "Reunión de equipo")  # Asigna una tarea al agente 1
    entorno.asignar_tarea(agente_2, "Preparación de informe")  # Asigna una tarea al agente 2
    entorno.asignar_tarea(agente_3, "Investigación de mercado")  # Asigna una tarea al agente 3

    # Se imprimen las tareas asignadas a cada agente
    agente_1.imprimir_tareas()  # Imprime las tareas del agente 1
    agente_2.imprimir_tareas()  # Imprime las tareas del agente 2
    agente_3.imprimir_tareas()  # Imprime las tareas del agente 3

if __name__ == "__main__":
    main()  # Llama a la función main si este script es ejecutado directamente
