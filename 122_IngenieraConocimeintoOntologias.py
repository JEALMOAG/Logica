"""
Created on 19 April  12:14:42 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
Este código implementa una base de conocimientos que almacena hechos sobre 
diferentes sujetos. Cada sujeto puede tener múltiples hechos asociados con él,
 y estos hechos se pueden agregar y consultar en la base de conocimientos. Por
 ejemplo, se pueden consultar hechos como qué tipo de objeto es un perro, qué 
 características tiene un gato, qué acciones realiza un perro, qué comen los gatos
 , etc. El sistema de base de conocimientos proporciona respuestas basadas en 
 los hechos que se han agregado previamente.
'''
class BaseConocimientos:
    def __init__(self):
        # Inicializa la base de conocimientos como un diccionario vacío
        self.base_conocimientos = {}

    def agregar_hecho(self, sujeto, hecho, objeto):
        # Agrega un hecho al diccionario de la base de conocimientos
        if sujeto not in self.base_conocimientos:
            self.base_conocimientos[sujeto] = {}  # Si el sujeto no está en la base de conocimientos, crea una entrada para él
        if hecho not in self.base_conocimientos[sujeto]:
            self.base_conocimientos[sujeto][hecho] = set()  # Si el hecho no está en el sujeto, crea una entrada para él
        self.base_conocimientos[sujeto][hecho].add(objeto)  # Agrega el objeto al hecho

    def consultar(self, sujeto, hecho):
        # Consulta la base de conocimientos para obtener información sobre un hecho específico de un sujeto
        if sujeto in self.base_conocimientos and hecho in self.base_conocimientos[sujeto]:
            return self.base_conocimientos[sujeto][hecho]  # Devuelve el conjunto de objetos relacionados con el hecho
        else:
            return set()  # Devuelve un conjunto vacío si no hay información sobre el hecho

# Crear una instancia de la base de conocimientos
base_conocimientos = BaseConocimientos()

# Agregar hechos a la base de conocimientos
base_conocimientos.agregar_hecho("Perro", "es_un", "Animal")  # El perro es un animal
base_conocimientos.agregar_hecho("Perro", "tiene", "Cuatro patas")  # Los perros tienen cuatro patas
base_conocimientos.agregar_hecho("Perro", "hace", "Ladrar")  # Los perros ladran
base_conocimientos.agregar_hecho("Perro", "come", "Carne")  # Los perros comen carne
base_conocimientos.agregar_hecho("Gato", "es_un", "Animal")  # El gato es un animal
base_conocimientos.agregar_hecho("Gato", "tiene", "Cuatro patas")  # Los gatos tienen cuatro patas
base_conocimientos.agregar_hecho("Gato", "hace", "Maullar")  # Los gatos maúllan
base_conocimientos.agregar_hecho("Gato", "come", "Pescado")  # Los gatos comen pescado

# Consultar la base de conocimientos
print("El perro es un:", base_conocimientos.consultar("Perro", "es_un"))  # Consulta si el perro es un animal
print("El gato tiene:", base_conocimientos.consultar("Gato", "tiene"))  # Consulta si el gato tiene cuatro patas
print("¿Qué hace un perro?", base_conocimientos.consultar("Perro", "hace"))  # Consulta qué hacen los perros
print("¿Qué hace un gato?", base_conocimientos.consultar("Gato", "hace"))  # Consulta qué hacen los gatos
print("¿Qué come un perro?", base_conocimientos.consultar("Perro", "come"))  # Consulta qué comen los perros
print("¿Qué come un gato?", base_conocimientos.consultar("Gato", "come"))  # Consulta qué comen los gatos

