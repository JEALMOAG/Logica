"""
Created on 19 April  19:40:49 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
El código representa un sistema de registro de personas y sus atributos.
 Utiliza dos clases: `Persona` y `RegistroPersonas`. La clase `Persona` representa
 a una persona con un nombre y un conjunto de atributos, y la clase `RegistroPersonas`
 gestiona un diccionario de personas, permitiendo agregar nuevas personas, 
 buscar personas por nombre, agregar atributos a personas existentes y mostrar todas
 las personas registradas junto con sus atributos.
'''

class Persona:
    def __init__(self, nombre, atributos=None): # Define la clase Persona con un constructor que recibe un nombre y atributos opcionales
        self.nombre = nombre # Asigna el nombre de la persona
        self.atributos = atributos if atributos is not None else {} # Asigna los atributos de la persona, si se proporcionan; de lo contrario, crea un diccionario vacío

    def agregar_atributo(self, clave, valor): # Método para agregar un atributo a la persona
        self.atributos[clave] = valor # Asigna el valor al atributo especificado

    def __str__(self): # Método para representar la persona como una cadena
        return f"{self.nombre}: {self.atributos}" # Retorna una cadena que muestra el nombre de la persona y sus atributos

class RegistroPersonas:
    def __init__(self): # Define la clase RegistroPersonas con un constructor
        self.personas = {} # Inicializa un diccionario para almacenar las personas

    def agregar_persona(self, nombre, atributos=None): # Método para definir una nueva persona en el registro
        persona = Persona(nombre, atributos) # Crea un nuevo objeto Persona con el nombre y atributos dados
        self.personas[nombre] = persona # Agrega la persona al diccionario de personas, utilizando el nombre como clave

    def encontrar_persona(self, nombre): # Método para encontrar una persona por su nombre
        return self.personas.get(nombre) # Retorna la persona correspondiente al nombre dado, si existe

    def agregar_atributo_a_persona(self, nombre_persona, clave, valor): # Método para agregar un atributo a una persona existente
        persona = self.encontrar_persona(nombre_persona) # Encuentra la persona con el nombre dado
        if persona: # Verifica si se encontró la persona
            persona.agregar_atributo(clave, valor) # Llama al método agregar_atributo de la persona encontrada
        else:
            print(f"Error: Persona '{nombre_persona}' no encontrada.") # Imprime un mensaje de error si la persona no se encuentra

    def mostrar_personas(self): # Método para mostrar todas las personas en el registro
        for nombre, persona in self.personas.items(): # Itera sobre cada par clave-valor en el diccionario de personas
            print(persona) # Imprime la persona

# Crear un registro de personas
registro = RegistroPersonas()

# Agregar personas y sus atributos
registro.agregar_persona("Juan", {"edad": 30, "profesion": "ingeniero"})
registro.agregar_persona("María", {"edad": 25, "profesion": "abogada"})
registro.agregar_persona("Carlos", {"edad": 35, "profesion": "médico"})

# Agregar más atributos a una persona
registro.agregar_atributo_a_persona("Juan", "hobby", "fotografía")
registro.agregar_atributo_a_persona("María", "hobby", "pintura")

# Mostrar el registro de personas
registro.mostrar_personas()
