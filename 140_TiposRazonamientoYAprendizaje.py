"""
created on 23 Abril 22:23:28 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código implementa un algoritmo de aprendizaje inductivo para identificar
animales mamíferos basándose en características como el pelaje y el número de
extremidades. Utiliza una clase Animal para representar los atributos de los
animales y define funciones para determinar si un animal es un mamífero y para
mostrar los resultados del aprendizaje.
"""
class Animal:  # Define una clase llamada Animal
    def __init__(self, nombre, tipo, pelaje, extremidades):  # Define el método de inicialización de la clase Animal con atributos nombre, tipo, pelaje y extremidades
        self.nombre = nombre  # Asigna el nombre del animal
        self.tipo = tipo  # Asigna el tipo del animal (por ejemplo, mamífero, ave, reptil)
        self.pelaje = pelaje  # Indica si el animal tiene pelaje (True o False)
        self.extremidades = extremidades  # Indica el número de extremidades del animal

# Datos de entrenamiento
animales_entrenamiento = [  # Lista de objetos de la clase Animal que representan animales con atributos específicos
    Animal("Perro", "mamífero", True, 4),  # Ejemplo de un perro, un mamífero con pelaje y cuatro extremidades
    Animal("Gato", "mamífero", True, 4),  # Ejemplo de un gato, un mamífero con pelaje y cuatro extremidades
    Animal("Pato", "ave", False, 2),  # Ejemplo de un pato, un ave sin pelaje y con dos extremidades
    Animal("Ballena", "mamífero", False, 0),  # Ejemplo de una ballena, un mamífero sin pelaje y sin extremidades (nadador)
    Animal("Cebra", "mamífero", True, 4),  # Ejemplo de una cebra, un mamífero con pelaje y cuatro extremidades
    Animal("Tortuga", "reptil", False, 4)  # Ejemplo de una tortuga, un reptil sin pelaje y con cuatro extremidades
]

# Función para determinar si un animal es un mamífero basado en características
def es_mamifero(animal):  # Define una función que toma un objeto Animal y devuelve True si es mamífero, False en caso contrario
    return animal.pelaje and animal.extremidades == 4  # Retorna True si el animal tiene pelaje y cuatro extremidades, False en caso contrario

# Algoritmo de aprendizaje inductivo
def aprendizaje_inductivo(animales):  # Define una función que toma una lista de animales y retorna una lista de mamíferos identificados
    mamiferos_identificados = []  # Inicializa una lista vacía para almacenar los mamíferos identificados
    for animal in animales:  # Itera sobre cada animal en la lista de animales
        if es_mamifero(animal):  # Verifica si el animal es un mamífero usando la función es_mamifero
            mamiferos_identificados.append(animal.nombre)  # Agrega el nombre del animal a la lista de mamíferos identificados
    return mamiferos_identificados  # Retorna la lista de mamíferos identificados

# Función para mostrar resultados
def mostrar_resultados(mamiferos_identificados):  # Define una función que muestra los mamíferos identificados
    if len(mamiferos_identificados) > 0:  # Verifica si se identificaron mamíferos
        print("Los siguientes animales son identificados como mamíferos:")  # Imprime un mensaje indicando que se identificaron mamíferos
        for animal in mamiferos_identificados:  # Itera sobre cada mamífero identificado
            print("- " + animal)  # Imprime el nombre del mamífero
    else:  # Si no se identificaron mamíferos
        print("No se identificaron mamíferos en el conjunto de datos de entrada.")  # Imprime un mensaje indicando que no se identificaron mamíferos

# Ejecución del programa
mamiferos_identificados = aprendizaje_inductivo(animales_entrenamiento)  # Llama a la función aprendizaje_inductivo con los datos de entrenamiento
mostrar_resultados(mamiferos_identificados)  # Muestra los resultados del aprendizaje inductivo

