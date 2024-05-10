"""
Created on 18 April  21:17:10 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
El código simula un sistema de recomendación de películas con lógica no monotónica,
 donde el Usuario recibe recomendaciones basadas en su historial de visualización, 
 pero la base de conocimiento del usuario puede cambiar con el tiempo. La clase 
 BaseConocimiento almacena las películas vistas por el usuario, y la clase Usuario 
 recibe y evalúa las recomendaciones, mostrando un mensaje indicando si la película
 recomendada ya ha sido vista en el historial actual o es una nueva sugerencia.
 '''
# Definición de la clase BaseConocimiento que representa la base de conocimiento del sistema de recomendación
class BaseConocimiento:
    def __init__(self):
        # Constructor de la clase BaseConocimiento
        self.peliculas_vistas = []  # Lista para almacenar las películas vistas por el usuario

    def agregar_pelicula_vista(self, pelicula):
        # Método para agregar una película vista a la base de conocimiento
        self.peliculas_vistas.append(pelicula)

    def consultar_pelicula_vista(self, pelicula):
        # Método para consultar si una película ha sido vista por el usuario
        return pelicula in self.peliculas_vistas

# Definición de la clase Agente que representa al usuario del sistema de recomendación
class Usuario:
    def __init__(self, base_conocimiento):
        # Constructor de la clase Usuario
        self.base_conocimiento = base_conocimiento  # La base de conocimiento asociada al usuario

    def recibir_recomendacion(self, pelicula):
        # Método para recibir una recomendación de película basada en el historial de visualización
        if self.base_conocimiento.consultar_pelicula_vista(pelicula):
            # Verifica si la película recomendada ha sido vista por el usuario
            print(f"¡Recomendación recibida! Te recomendamos ver: {pelicula}")
        else:
            print(f"¡Nueva recomendación! Te sugerimos ver: {pelicula}")

# Crear una base de conocimiento del usuario
base_conocimiento_usuario = BaseConocimiento()

# Agregar películas vistas al historial del usuario
base_conocimiento_usuario.agregar_pelicula_vista("Matrix")
base_conocimiento_usuario.agregar_pelicula_vista("Interestelar")

# Crear un usuario con la base de conocimiento
usuario = Usuario(base_conocimiento_usuario)

# Recibir recomendaciones de películas
usuario.recibir_recomendacion("Matrix")  # El usuario recibe una recomendación para ver Matrix
usuario.recibir_recomendacion("Inception")  # El usuario recibe una recomendación para ver Inception, una película nueva para él
