"""
created on 27 Abril 14:37:04 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código define una clase llamada GramaticaCausal que genera oraciones
aleatorias en español con una estructura causal. Utiliza listas de sujetos,
verbos y objetos predefinidos, así como una lista de posibles causas.
La función generar_oracion() selecciona aleatoriamente un sujeto, verbo,
objeto y causa, y los concatena para formar una oración causal.
Finalmente, se muestra un ejemplo de uso generando cinco oraciones diferentes.
"""
import random  # Importamos el módulo random para generar números aleatorios

class GramaticaCausal:  # Definimos la clase GramaticaCausal
    def __init__(self):  # Definimos el método constructor de la clase
        # Listas de sujetos, verbos y objetos
        self.sujetos = ['El gato', 'El perro', 'La tortuga', 'El pájaro', 'El pez']
        self.verbos = ['persiguió', 'atrapó', 'comió', 'miró', 'asustó']
        self.objetos = ['el ratón', 'la mariposa', 'la comida', 'la pelota', 'la presa']

    def generar_oracion(self):  # Definimos el método para generar una oración
        sujeto = random.choice(self.sujetos)  # Seleccionamos aleatoriamente un sujeto
        verbo = random.choice(self.verbos)  # Seleccionamos aleatoriamente un verbo
        objeto = random.choice(self.objetos)  # Seleccionamos aleatoriamente un objeto

        return f"{sujeto} {verbo} {objeto} porque {self._generar_causa()}."  # Concatenamos las partes de la oración con una causa

    def _generar_causa(self):  # Definimos un método privado para generar una causa
        # Lista de posibles causas
        causas = [
            "estaba hambriento",
            "quería jugar",
            "se sintió amenazado",
            "escuchó un ruido",
            "vio movimiento"
        ]
        return random.choice(causas)  # Seleccionamos aleatoriamente una causa

# Ejemplo de uso
gramatica = GramaticaCausal()  # Creamos una instancia de la clase GramaticaCausal

for _ in range(5):  # Generamos 5 oraciones
    oracion = gramatica.generar_oracion()  # Generamos una oración
    print(oracion)  # Imprimimos la oración






