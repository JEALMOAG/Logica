"""
Created on 20 April  10:15:13 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
El código define una clase llamada `KnowledgeBase`, que representa una base de 
conocimiento médico para diagnosticar enfermedades a partir de síntomas. Permite 
agregar reglas que relacionan enfermedades con sus síntomas y realizar diagnósticos
 basados en síntomas proporcionados. Cada regla asocia una enfermedad con una lista
 de síntomas. Al realizar un diagnóstico, se comparan los síntomas proporcionados
 con los síntomas de cada enfermedad en la base de conocimiento para encontrar 
 coincidencias exactas y determinar la enfermedad diagnosticada.
'''
class KnowledgeBase:
    def __init__(self):
        self.rules = {}  # Diccionario para almacenar reglas (enfermedad -> síntomas)

    def add_rule(self, disease, symptoms):
        self.rules[disease] = symptoms  # Agrega una regla que asocia una enfermedad con sus síntomas

    def infer_disease(self, symptoms):
        # Busca la enfermedad que coincide con los síntomas proporcionados
        for disease, symptoms_list in self.rules.items():
            if set(symptoms) == set(symptoms_list):  # Compara si los síntomas coinciden exactamente con los síntomas de la enfermedad
                return disease  # Devuelve la enfermedad si hay una coincidencia exacta
        return "No se puede diagnosticar la enfermedad"  # Si no se encuentran coincidencias, devuelve un mensaje de error

# Creamos una base de conocimiento
kb = KnowledgeBase()

# Añadimos reglas para algunas enfermedades y sus síntomas
kb.add_rule("Resfriado", ["Congestión nasal", "Estornudos", "Garganta irritada"])
kb.add_rule("Gripe", ["Fiebre", "Dolor de cabeza", "Dolor muscular"])
kb.add_rule("Alergia", ["Estornudos", "Picazón en los ojos", "Secreción nasal"])

# Realizamos algunas consultas de diagnóstico
print("Diagnóstico para síntomas [Congestión nasal, Estornudos, Garganta irritada]:")
print("Enfermedad diagnosticada:", kb.infer_disease(["Congestión nasal", "Estornudos", "Garganta irritada"]))

print("\nDiagnóstico para síntomas [Fiebre, Dolor de cabeza, Dolor muscular]:")
print("Enfermedad diagnosticada:", kb.infer_disease(["Fiebre", "Dolor de cabeza", "Dolor muscular"]))

print("\nDiagnóstico para síntomas [Estornudos, Picazón en los ojos, Secreción nasal]:")
print("Enfermedad diagnosticada:", kb.infer_disease(["Estornudos", "Picazón en los ojos", "Secreción nasal"]))

print("\nDiagnóstico para síntomas [Fiebre, Estornudos, Dolor de cabeza]:")
print("Enfermedad diagnosticada:", kb.infer_disease(["Fiebre", "Estornudos", "Dolor de cabeza"]))
