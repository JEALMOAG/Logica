"""
Created on 19 April  01:13:11 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
El código simula un sistema de sensibilidades sensoriales donde se definen 
diferentes niveles de sensibilidad sensorial, cada uno con una función específica 
que modela la percepción de estímulos en un rango de intensidades. Luego, se 
calcula la sensibilidad para un valor dado en cada sensibilidad sensorial.
'''
class SensibilidadSensorial:
    def __init__(self, nombre, funcion_sensibilidad):
        self.nombre = nombre  # Nombre de la sensibilidad sensorial
        self.funcion_sensibilidad = funcion_sensibilidad  # Función de sensibilidad sensorial

    def sensibilidad(self, valor):
        return self.funcion_sensibilidad(valor)  # Calcula la sensibilidad para un valor dado


# Definir funciones de sensibilidad sensorial
def baja_sensibilidad(inicio, pico, fin):
    def funcion(valor):
        if valor <= inicio or valor >= fin:  # Si el valor está fuera del rango de sensibilidad baja
            return 0
        elif inicio < valor < pico:  # Si el valor está dentro de la pendiente ascendente de sensibilidad baja
            return (valor - inicio) / (pico - inicio)  # Calcula la sensibilidad basada en la pendiente ascendente
        elif pico <= valor <= fin:  # Si el valor está dentro de la pendiente descendente de sensibilidad baja
            return (fin - valor) / (fin - pico)  # Calcula la sensibilidad basada en la pendiente descendente
        else:
            return 0  # Si el valor está fuera del rango de sensibilidad baja
    return funcion


def alta_sensibilidad(inicio, pico, fin):
    def funcion(valor):
        if valor <= inicio or valor >= fin:  # Si el valor está fuera del rango de sensibilidad alta
            return 0
        elif inicio < valor < pico:  # Si el valor está dentro de la pendiente ascendente de sensibilidad alta
            return (valor - inicio) / (pico - inicio)  # Calcula la sensibilidad basada en la pendiente ascendente
        elif pico <= valor <= fin:  # Si el valor está dentro de la pendiente descendente de sensibilidad alta
            return (fin - valor) / (fin - pico)  # Calcula la sensibilidad basada en la pendiente descendente
        else:
            return 1  # Si el valor está dentro del rango horizontal de sensibilidad alta
    return funcion


# Crear sensibilidades sensoriales
sensor_vision = SensibilidadSensorial("Visión", baja_sensibilidad(0, 0, 10))  # Crear una sensibilidad sensorial de visión con una función de baja sensibilidad
sensor_tacto = SensibilidadSensorial("Tacto", alta_sensibilidad(5, 10, 15))  # Crear una sensibilidad sensorial de tacto con una función de alta sensibilidad

# Calcular sensibilidad para un valor dado en cada sensibilidad sensorial
intensidad_estimulo = 8
print(f"La sensibilidad para un estímulo de intensidad {intensidad_estimulo} en {sensor_vision.nombre} es: {sensor_vision.sensibilidad(intensidad_estimulo)}")  # Calcular la sensibilidad para el estímulo de intensidad en la sensibilidad sensorial de visión
print(f"La sensibilidad para un estímulo de intensidad {intensidad_estimulo} en {sensor_tacto.nombre} es: {sensor_tacto.sensibilidad(intensidad_estimulo)}")  # Calcular la sensibilidad para el estímulo de intensidad en la sensibilidad sensorial de tacto
