"""
Created on 18 April  09:18:51 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
En este código, se definen dos clases: `Mundo` y `Agente`. La clase `Mundo`
 representa un mundo en la lógica modal, con un nombre y conexiones a otros 
 mundos. La clase `Agente` representa un agente en ese mundo, con un nombre y
 una ubicación actual en uno de los mundos. Se crean varios mundos y se establecen
 conexiones entre ellos. Luego, se crea un agente que se mueve entre los mundos,
 mostrando mensajes de movimiento exitoso o errores si no es posible realizar el 
 movimiento.
'''
# Definición de la clase Mundo que representa un mundo en la lógica modal
class Mundo:
    def __init__(self, nombre, conexiones=None):
        # Constructor de la clase Mundo
        self.nombre = nombre  # Nombre del mundo
        self.conexiones = conexiones if conexiones else []  # Lista de mundos conectados a este mundo

    def agregar_conexion(self, mundo):
        # Método para agregar un mundo conectado a este mundo
        self.conexiones.append(mundo)

# Definición de la clase Agente que representa un agente en la lógica modal
class Agente:
    def __init__(self, nombre, ubicacion_actual):
        # Constructor de la clase Agente
        self.nombre = nombre  # Nombre del agente
        self.ubicacion_actual = ubicacion_actual  # Mundo en el que se encuentra el agente

    def moverse_a_mundo(self, mundo):
        # Método para que el agente se mueva a otro mundo
        if mundo in self.ubicacion_actual.conexiones:
            # Verifica si el mundo al que el agente quiere ir está conectado desde la ubicación actual
            self.ubicacion_actual = mundo  # El agente se mueve al nuevo mundo
            print(f"{self.nombre} se mueve al mundo {mundo.nombre}")  # Mensaje de movimiento exitoso
        else:
            print(f"¡Error! {self.nombre} no puede ir al mundo {mundo.nombre}")
            # Mensaje de error si el mundo al que el agente quiere ir no está conectado desde la ubicación actual

# Definición de mundos
mundo_a = Mundo("Mundo A")  # Creamos el Mundo A
mundo_b = Mundo("Mundo B")  # Creamos el Mundo B
mundo_c = Mundo("Mundo C")  # Creamos el Mundo C

# Conexiones entre mundos
mundo_a.agregar_conexion(mundo_b)  # Hacemos el Mundo B accesible desde el Mundo A
mundo_b.agregar_conexion(mundo_c)  # Hacemos el Mundo C accesible desde el Mundo B
mundo_c.agregar_conexion(mundo_a)  # Hacemos el Mundo A accesible desde el Mundo C, creando un ciclo

# Crear un agente
agente_principal = Agente("Agente Principal", mundo_a)  # Creamos el Agente Principal en el Mundo A

# Ejemplo de movimiento del agente
agente_principal.moverse_a_mundo(mundo_b)  # El agente se mueve al Mundo B
agente_principal.moverse_a_mundo(mundo_c)  # El agente se mueve al Mundo C
agente_principal.moverse_a_mundo(mundo_a)  # El agente no puede ir al Mundo A desde Mundo C, ya que Mundo A no está conectado desde Mundo C
