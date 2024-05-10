"""
Created on 19 April  21:58:53 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
El código simula un sistema de registro de opiniones, donde se definen clases 
para representar opiniones y un registro para almacenar y consultar estas opiniones.
 Cada opinión está compuesta por un sujeto (quien emite la opinión), un objeto
 (el tema de la opinión) y un predicado (la naturaleza de la opinión).
 Las opiniones se agregan al registro y luego se pueden consultar.
'''
class Opinion:
    def __init__(self, sujeto, objeto, predicado):
        self.sujeto = sujeto  # El individuo que emite la opinión
        self.objeto = objeto  # El tema o asunto sobre el que se emite la opinión
        self.predicado = predicado  # La naturaleza de la opinión

    def __str__(self):
        return f"({self.sujeto}, {self.predicado}, {self.objeto})"  # Representación en cadena de la opinión

class RegistroOpiniones:
    def __init__(self):
        self.opiniones = []  # Lista para almacenar las opiniones

    def agregar_opinion(self, opinion):
        self.opiniones.append(opinion)  # Agrega una nueva opinión a la lista

    def consultar_opiniones(self):
        for opinion in self.opiniones:
            print(opinion)  # Imprime cada opinión en la lista

# Crear un registro de opiniones
registro_opiniones = RegistroOpiniones()

# Agregar opiniones al registro
registro_opiniones.agregar_opinion(Opinion("Juan", "pizza", "le gusta"))  # Juan le gusta la pizza
registro_opiniones.agregar_opinion(Opinion("María", "guitarra", "toca"))  # María toca la guitarra
registro_opiniones.agregar_opinion(Opinion("Ana", "libro", "lee"))  # Ana lee libros

# Consultar las opiniones en el registro
print("Opiniones en el registro:")
registro_opiniones.consultar_opiniones()
