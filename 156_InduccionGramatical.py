"""
created on 28 Abril 09:27:56 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código define una clase llamada InduccionGramatical, la cual se utiliza para
realizar la inducción gramatical a partir de ejemplos de texto proporcionados.
Esta clase tiene métodos para agregar ejemplos y para inducir la gramática
basada en esos ejemplos. La función principal inducir_gramatica analiza los
ejemplos y construye una gramática simple que describe la secuencia de palabras
en los ejemplos. Luego, se muestran las reglas gramaticales inducidas.
"""
class InduccionGramatical:  # Definimos la clase InduccionGramatical para la inducción gramatical
    def __init__(self):  # Definimos el método constructor de la clase
        self.ejemplos = []  # Inicializamos una lista para almacenar los ejemplos de texto

    def agregar_ejemplo(self, ejemplo):  # Definimos el método para agregar un ejemplo
        self.ejemplos.append(ejemplo)  # Agregamos el ejemplo a la lista de ejemplos

    def inducir_gramatica(self):  # Definimos el método para inducir la gramática a partir de los ejemplos
        if not self.ejemplos:  # Verificamos si hay ejemplos
            return "No hay ejemplos para inducir la gramática."  # Si no hay ejemplos, retornamos un mensaje indicando la ausencia de ejemplos

        gramatica = {}  # Creamos un diccionario para almacenar la gramática inducida
        for ejemplo in self.ejemplos:  # Iteramos sobre cada ejemplo
            palabras = ejemplo.split()  # Dividimos el ejemplo en palabras
            for i in range(len(palabras) - 1):  # Iteramos sobre cada palabra en el ejemplo, excepto la última
                palabra_actual = palabras[i]  # Obtenemos la palabra actual
                palabra_siguiente = palabras[i + 1]  # Obtenemos la palabra siguiente

                if palabra_actual not in gramatica:  # Verificamos si la palabra actual no está en la gramática
                    gramatica[palabra_actual] = []  # Si no está, creamos una entrada para la palabra actual en la gramática

                if palabra_siguiente not in gramatica[palabra_actual]:  # Verificamos si la palabra siguiente no está en las opciones de palabras siguientes para la palabra actual
                    gramatica[palabra_actual].append(palabra_siguiente)  # Si no está, la agregamos a las opciones de palabras siguientes para la palabra actual

        return gramatica  # Retornamos la gramática inducida como un diccionario

# Ejemplo de uso
inductor = InduccionGramatical()  # Creamos una instancia de la clase InduccionGramatical

# Agregamos ejemplos
inductor.agregar_ejemplo("El gato persigue al ratón")
inductor.agregar_ejemplo("La niña juega con la pelota")

# Realizamos la inducción de la gramática
gramatica = inductor.inducir_gramatica()

# Mostramos la gramática inducida
print("Gramática Inducida:")
for clave, valor in gramatica.items():
    print(f"{clave} -> {' | '.join(valor)}")  # Imprimimos las reglas gramaticales inducidas
