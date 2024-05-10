"""
Created on 18 April  02:29:19 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
En este código, se han cambiado los nombres de las personas a "Pedro" y "Sofía".
 Ahora la base de conocimiento y las consultas utilizan estos nuevos nombres.
 El agente lógico todavía funciona de la misma manera, realizando inferencias 
 sobre la base de conocimiento y devolviendo los resultados correspondientes.
'''
class LogicalAgent:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base  # Inicializa la base de conocimiento del agente

    def infer(self, query):
        # Implementar el motor de inferencia lógica aquí
        # Puede ser un algoritmo de encadenamiento hacia adelante, hacia atrás, resolución, etc.
        # Por simplicidad, este ejemplo utilizará una búsqueda en la base de conocimiento

        # Comprueba si la consulta está en la base de conocimiento
        if query in self.knowledge_base:  # Si la consulta está en la base de conocimiento
            return True  # Devuelve verdadero
        else:  # Si la consulta no está en la base de conocimiento
            return False  # Devuelve falso

# Ejemplo de uso
if __name__ == "__main__":
    # Base de conocimiento
    knowledge_base = {
        "Man(Pedro)",
        "Woman(Sofía)",
        "Father(Pedro, Carlos)",
        "Mother(Sofía, Carlos)",
        "Father(Pedro, Laura)",
        "Mother(Sofía, Laura)"
    }  # Define una base de conocimiento con hechos lógicos

    # Crear un agente lógico con la base de conocimiento
    agent = LogicalAgent(knowledge_base)  # Crea una instancia de la clase LogicalAgent

    # Consultas
    query1 = "Man(Pedro)"         # Consulta sobre si Pedro es un hombre
    query2 = "Father(Pedro, Carlos)"  # Consulta sobre si Pedro es el padre de Carlos
    query3 = "Man(Sofía)"         # Consulta sobre si Sofía es un hombre

    # Realizar inferencias
    result1 = agent.infer(query1)  # Realiza una inferencia sobre consulta1
    result2 = agent.infer(query2)  # Realiza una inferencia sobre consulta2
    result3 = agent.infer(query3)  # Realiza una inferencia sobre consulta3

    # Mostrar resultados
    print(f"¿{query1}? {result1}")  # Muestra si Pedro es un hombre
    print(f"¿{query2}? {result2}")  # Muestra si Pedro es el padre de Carlos
    print(f"¿{query3}? {result3}")  # Muestra si Sofía es un hombre (falso)
