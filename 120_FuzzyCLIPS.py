"""
Created on 19 April  07:02:57 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
Este código implementa un sistema de control difuso para regular la intensidad 
de una lámpara en función de la luminosidad del entorno. Utiliza funciones de 
pertenencia para definir la relación entre la luminosidad y la intensidad de la 
lámpara, luego evalúa reglas difusas para determinar la intensidad óptima de la 
lámpara. Finalmente, utiliza el método de defuzzificación del centroide para 
calcular la intensidad final de la lámpara y simula su funcionamiento para una
 luminosidad específica.
'''
# Funciones de pertenencia para la luminosidad
def membership_light_low(light):
    if light <= 50:
        return 1  # Si la luminosidad es menor o igual a 50, la membresía es 1
    elif light > 50 and light < 70:
        return (70 - light) / (70 - 50)  # Calcula la membresía de manera lineal entre 1 y 0 en el rango de 50 a 70
    else:
        return 0  # Si la luminosidad es mayor o igual a 70, la membresía es 0

def membership_light_medium(light):
    if light <= 50 or light >= 90:
        return 0  # Si la luminosidad es menor o igual a 50, o mayor o igual a 90, la membresía es 0
    elif light > 50 and light < 70:
        return (light - 50) / (70 - 50)  # Calcula la membresía de manera lineal entre 0 y 1 en el rango de 50 a 70
    elif light >= 70 and light <= 90:
        return 1  # Si la luminosidad está entre 70 y 90, la membresía es 1
    else:
        return 0  # Si la luminosidad es menor a 70 o mayor a 90, la membresía es 0

def membership_light_high(light):
    if light <= 70:
        return 0  # Si la luminosidad es menor o igual a 70, la membresía es 0
    elif light > 70 and light < 90:
        return (light - 70) / (90 - 70)  # Calcula la membresía de manera lineal entre 0 y 1 en el rango de 70 a 90
    else:
        return 1  # Si la luminosidad es mayor o igual a 90, la membresía es 1

# Funciones de pertenencia para la intensidad de la luz de la lámpara
def membership_lamp_intensity_low(intensity):
    if intensity <= 50:
        return 1  # Si la intensidad es menor o igual a 50, la membresía es 1
    elif intensity > 50 and intensity < 70:
        return (70 - intensity) / (70 - 50)  # Calcula la membresía de manera lineal entre 1 y 0 en el rango de 50 a 70
    else:
        return 0  # Si la intensidad es mayor o igual a 70, la membresía es 0

def membership_lamp_intensity_medium(intensity):
    if intensity <= 50 or intensity >= 90:
        return 0  # Si la intensidad es menor o igual a 50, o mayor o igual a 90, la membresía es 0
    elif intensity > 50 and intensity < 70:
        return (intensity - 50) / (70 - 50)  # Calcula la membresía de manera lineal entre 0 y 1 en el rango de 50 a 70
    elif intensity >= 70 and intensity <= 90:
        return 1  # Si la intensidad está entre 70 y 90, la membresía es 1
    else:
        return 0  # Si la intensidad es menor a 70 o mayor a 90, la membresía es 0

def membership_lamp_intensity_high(intensity):
    if intensity <= 70:
        return 0  # Si la intensidad es menor o igual a 70, la membresía es 0
    elif intensity > 70 and intensity < 90:
        return (intensity - 70) / (90 - 70)  # Calcula la membresía de manera lineal entre 0 y 1 en el rango de 70 a 90
    else:
        return 1  # Si la intensidad es mayor o igual a 90, la membresía es 1

# Inferencia difusa
def fuzzy_inference(light):
    # Evaluación de las reglas difusas
    low_intensity = min(membership_light_low(light), membership_lamp_intensity_low(light))
    medium_intensity = min(membership_light_medium(light), membership_lamp_intensity_medium(light))
    high_intensity = min(membership_light_high(light), membership_lamp_intensity_high(light))

    # Defuzzification (Centroide)
    numerator = low_intensity * 25 + medium_intensity * 60 + high_intensity * 85
    denominator = low_intensity + medium_intensity + high_intensity
    if denominator == 0:
        return 0
    return numerator / denominator

# Simulación
light_intensity = 75
lamp_intensity = fuzzy_inference(light_intensity)
print("Lamp intensity:", lamp_intensity)
