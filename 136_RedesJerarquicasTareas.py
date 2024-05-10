"""
created on 23 Abril 06:23:48 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código define una clase Tarea para representar tareas con posibles sub tareas.
También incluye una función para ejecutar recursivamente estas tareas y sus
sub tareas. En el ejemplo de uso, se crea una tarea principal con sub tareas,
y luego se ejecuta la tarea principal, mostrando el nombre de cada tarea que
se ejecuta en orden.
"""
class Tarea:
    def __init__(self, nombre, subtareas=None):  # Define la clase Tarea con un constructor que recibe el nombre de la tarea y una lista opcional de sub tareas
        self.nombre = nombre  # Asigna el nombre de la tarea al atributo nombre
        self.subtareas = subtareas if subtareas else []  # Asigna la lista de sub tareas al atributo subtareas, o crea una lista vacía si no se proporciona ninguna

    def agregar_subtarea(self, subtarea):  # Método para agregar una sub tarea a la lista de sub tareas
        self.subtareas.append(subtarea)  # Agrega la sub tarea a la lista de sub tareas de la tarea actual

    def __repr__(self):  # Método especial para representar la tarea como una cadena
        return f"Tarea({self.nombre}, {self.subtareas})"  # Retorna una cadena que representa la tarea y sus sub tareas

def ejecutar_tarea(tarea):  # Función para ejecutar una tarea y sus sub tareas recursivamente
    print(f"Ejecutando tarea: {tarea.nombre}")  # Imprime el nombre de la tarea actual
    for subtarea in tarea.subtareas:  # Itera sobre todas las sub tareas de la tarea actual
        ejecutar_tarea(subtarea)  # Llama recursivamente a ejecutar_tarea para ejecutar la sub tarea

# Ejemplo de uso
if __name__ == "__main__":
    tarea_principal = Tarea("Tarea Principal")  # Crea una tarea principal con el nombre "Tarea Principal"
    subtarea1 = Tarea("Subtarea 1")  # Crea una sub tarea con el nombre "Subtarea 1"
    subtarea2 = Tarea("Subtarea 2")  # Crea otra sub tarea con el nombre "Subtarea 2"
    sub_subtarea1 = Tarea("Sub-Subtarea 1")  # Crea una sub sub tarea con el nombre "Sub-Subtarea 1"
    sub_subtarea2 = Tarea("Sub-Subtarea 2")  # Crea otra sub sub tarea con el nombre "Sub-Subtarea 2"

    subtarea1.agregar_subtarea(sub_subtarea1)  # Agrega la sub sub tarea 1 a la lista de sub tareas de la sub tarea 1
    subtarea1.agregar_subtarea(sub_subtarea2)  # Agrega la sub sub tarea 2 a la lista de sub tareas de la sub tarea 1

    tarea_principal.agregar_subtarea(subtarea1)  # Agrega la sub tarea 1 a la lista de sub tareas de la tarea principal
    tarea_principal.agregar_subtarea(subtarea2)  # Agrega la sub tarea 2 a la lista de sub tareas de la tarea principal

    ejecutar_tarea(tarea_principal)  # Ejecuta la tarea principal y todas sus sub tareas recursivamente
