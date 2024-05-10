"""
Created on 18 April  13:14:11 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
Este código modela la lógica temporal con las clases `MundoTemporal` y `AgenteTemporal`. 
En la clase `MundoTemporal`, un mundo temporal contiene un nombre y una lista de eventos 
asociados. La clase `AgenteTemporal` representa un agente en este mundo, con un nombre y
 una ubicación en un mundo temporal. El agente puede ejecutar eventos presentes en el 
 mundo temporal actual.
'''

# Definición de la clase MundoTemporal que representa un mundo en la lógica temporal
class MundoTemporal:
    def __init__(self, nombre, eventos=None):
        # Constructor de la clase MundoTemporal
        self.nombre = nombre  # Nombre del mundo temporal
        self.eventos = eventos if eventos else []  # Lista de eventos en este mundo temporal

    def agregar_evento(self, evento):
        # Método para agregar un evento al mundo temporal
        self.eventos.append(evento)

# Definición de la clase AgenteTemporal que representa un agente en la lógica temporal
class AgenteTemporal:
    def __init__(self, nombre, mundo_actual):
        # Constructor de la clase AgenteTemporal
        self.nombre = nombre  # Nombre del agente temporal
        self.mundo_actual = mundo_actual  # Mundo temporal en el que se encuentra el agente

    def ejecutar_evento(self, evento):
        # Método para que el agente temporal ejecute un evento
        if evento in self.mundo_actual.eventos:
            # Verifica si el evento está presente en el mundo temporal actual
            print(f"Se activa el evento '{evento}' en respuesta a la acción del {self.nombre}.")  # Descripción de la activación del evento
        else:
            print(f"Se encuentra un error: el evento '{evento}' no está disponible en el Mundo Actual, y el {self.nombre} no puede ejecutarlo.")
            # Mensaje de error si el evento no está presente en el mundo temporal actual

# Definición de mundos temporales
mundo_actual = MundoTemporal("Mundo Actual", ["evento1", "evento2"])  # Creamos el Mundo Actual con eventos
mundo_futuro = MundoTemporal("Mundo Futuro")  # Creamos el Mundo Futuro sin eventos

# Crear un agente temporal
agente_temporal = AgenteTemporal("Agente Temporal", mundo_actual)  # Creamos el Agente Temporal en el Mundo Actual

# Ejemplo de ejecución de eventos por el agente
agente_temporal.ejecutar_evento("evento1")  # Se activa el evento "evento1" en respuesta a la acción del Agente Temporal.
agente_temporal.ejecutar_evento("evento3")  # Se encuentra un error: el evento "evento3" no está disponible en el Mundo Actual, y el Agente Temporal no puede ejecutarlo.

