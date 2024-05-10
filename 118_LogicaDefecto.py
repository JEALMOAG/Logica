"""
Created on 18 April  23:48:51 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
El código simula un sistema de diagnóstico médico donde se agregan reglas de
 diagnóstico a una base de conocimientos. Luego, se realiza una inferencia para 
 confirmar un diagnóstico médico basado en una consulta. Las reglas asociadas a 
 un diagnóstico dado se utilizan para confirmar la presencia de ese diagnóstico.
 '''
class SistemaDiagnóstico:
    def __init__(self):
        self.base_conocimiento = {}  # Base de conocimientos

    def agregar_regla(self, regla, diagnostico):
        if diagnostico not in self.base_conocimiento:
            self.base_conocimiento[diagnostico] = []  # Si el diagnóstico no está en la base de conocimientos, crea una nueva lista vacía para almacenar las reglas asociadas a ese diagnóstico
        self.base_conocimiento[diagnostico].append(regla)  # Agrega la regla a la lista de reglas asociadas al diagnóstico

    def inferir(self, consulta):
        if consulta in self.base_conocimiento:  # Si la consulta está en la base de conocimientos
            print("El diagnóstico se confirma debido a las siguientes reglas:")
            for regla in self.base_conocimiento[consulta]:  # Itera sobre todas las reglas asociadas a la consulta
                print("- ", regla)  # Imprime cada regla asociada a la consulta
        else:
            print("No se puede confirmar el diagnóstico.")  # Si la consulta no está en la base de conocimientos, imprime un mensaje indicando que no se puede confirmar

# Crear una instancia del sistema de diagnóstico
sistema_diagnostico = SistemaDiagnóstico()

# Agregar reglas a la base de conocimientos
sistema_diagnostico.agregar_regla("Si tiene fiebre y dolor de cabeza, entonces es gripe.", "gripe")
sistema_diagnostico.agregar_regla("Si tiene tos persistente y dificultad para respirar, entonces es neumonía.", "neumonía")

# Consulta
consulta = "gripe"
sistema_diagnostico.inferir(consulta)  # Realiza una inferencia basada en la consulta y muestra el resultado
