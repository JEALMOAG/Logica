"""
created on 27 Abril 23:38:18 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
Este código define una clase llamada AmbiguityResolver que se utiliza para
resolver ambigüedades en frases. El método resolve_ambiguity toma una frase
como entrada y devuelve una lista de interpretaciones posibles para esa frase.
En el ejemplo de uso, se instancia la clase AmbiguityResolver, se proporciona
una frase ambigua, y se obtienen e imprimen las interpretaciones posibles de la
frase.
"""
class ResolvedorAmbiguedad:  # Definimos la clase ResolvedorAmbiguedad
    def __init__(self):  # Definimos el método constructor de la clase
        pass  # No hay inicialización necesaria en este caso

    def resolver_ambiguedad(self, frase):  # Definimos el método para resolver la ambigüedad
        interpretaciones = []  # Creamos una lista para almacenar las interpretaciones posibles de la frase

        # Interpretación 1: "Vi a la mujer a través del telescopio."
        interpretacion_1 = "Vi a la mujer a través del telescopio."
        interpretaciones.append(interpretacion_1)  # Añadimos la interpretación a la lista de interpretaciones

        # Interpretación 2: "Vi a la mujer que estaba sosteniendo el telescopio."
        interpretacion_2 = "Vi a la mujer que estaba sosteniendo el telescopio."
        interpretaciones.append(interpretacion_2)  # Añadimos la interpretación a la lista de interpretaciones

        return interpretaciones  # Retornamos todas las interpretaciones posibles

# Ejemplo de uso
resolvedor = ResolvedorAmbiguedad()  # Creamos una instancia de la clase ResolvedorAmbiguedad

frase_ambigua = "Vi a la mujer con el telescopio."  # Definimos la frase ambigua
interpretaciones = resolvedor.resolver_ambiguedad(frase_ambigua)  # Resolvemos la ambigüedad

print("Frase ambigua:", frase_ambigua)  # Imprimimos la frase ambigua
print("Interpretaciones:")  # Imprimimos un mensaje indicando las interpretaciones posibles
for i, interpretacion in enumerate(interpretaciones, start=1):  # Iteramos sobre las interpretaciones posibles
    print(f"Interpretación {i}: {interpretacion}")  # Imprimimos cada interpretación con su índice
