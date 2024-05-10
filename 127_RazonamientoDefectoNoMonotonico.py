"""
Created on 19 April  00:11:11 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
Este código presenta una implementación básica de una base de conocimiento y 
reglas de inferencia.

La clase KnowledgeBase almacena hechos conocidos y reglas, tanto predeterminadas 
como no predeterminadas. Permite agregar hechos, reglas predeterminadas y no predeterminadas,
 y realizar inferencias sobre nuevos hechos.
La clase Rule representa una regla con una condición y un resultado. Tiene un método 
implies que verifica si el resultado de la regla coincide con un hecho consultado.
El código crea una instancia de KnowledgeBase, agrega reglas predeterminadas y no
 predeterminadas, así como un hecho inicial. Luego, realiza una consulta para 
 determinar si un pingüino vuela, basándose en las reglas establecidas y los hechos 
 conocidos.
'''
class KnowledgeBase:
    def __init__(self):
        self.facts = set()  # Conjunto para almacenar hechos conocidos
        self.default_rules = set()  # Conjunto para almacenar reglas predeterminadas
        self.non_default_rules = set()  # Conjunto para almacenar reglas no predeterminadas

    def add_fact(self, fact):
        self.facts.add(fact)  # Agrega un hecho a la base de conocimiento

    def add_default_rule(self, rule):
        self.default_rules.add(rule)  # Agrega una regla predeterminada a la base de conocimiento

    def add_non_default_rule(self, rule):
        self.non_default_rules.add(rule)  # Agrega una regla no predeterminada a la base de conocimiento

    def infer(self, fact):
        if fact in self.facts:  # Si el hecho es conocido, devuelve verdadero
            return True
        for rule in self.default_rules:  # Verifica las reglas predeterminadas
            if rule.implies(fact):  # Si la regla implica el hecho, devuelve verdadero
                return True
        return False  # Si ninguna regla implica el hecho, devuelve falso

class Rule:
    def __init__(self, condition, result):
        self.condition = condition  # Condición de la regla
        self.result = result  # Resultado de la regla

    def implies(self, fact):
        return self.result == fact  # Verifica si el resultado de la regla coincide con el hecho consultado

    def __str__(self):
        return f"{self.condition} -> {self.result}"  # Representación de cadena de la regla

# Creamos una base de conocimiento
kb = KnowledgeBase()

# Reglas predeterminadas
kb.add_default_rule(Rule("bird(X)", "flies(X)"))  # Si X es un pájaro, entonces X vuela
kb.add_default_rule(Rule("flies(X)", "bird(X)"))  # Si X vuela, entonces X es un pájaro

# Reglas no predeterminadas
kb.add_non_default_rule(Rule("bird(penguin)", "flies(penguin)"))  # Un pingüino es un pájaro, pero no vuela

# Hechos iniciales
kb.add_fact("bird(penguin)")  # El hecho de que un pingüino sea un pájaro

# Consulta si un pingüino vuela
if kb.infer("flies(penguin)"):  # Verifica si se deduce que un pingüino vuela
    print("El pingüino vuela.")
else:
    print("El pingüino no vuela.")