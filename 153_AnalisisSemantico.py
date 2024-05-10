"""
created on 27 Abril 10:58:28 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código define una clase llamada AnalizadorSemantico que analiza una oración
en busca de palabras clave predefinidas y sus significados. La clase contiene
un diccionario de palabras clave y sus significados. El método analizar_oracion
analiza una oración dada, identifica las palabras clave presentes y devuelve
una lista de tuplas que contienen la palabra clave encontrada y su significado.
Finalmente, se muestra el resultado del análisis semántico de la oración de
ejemplo, indicando las palabras clave encontradas y sus significados asociados.
"""
class AnalizadorSemantico:  # Definición de la clase AnalizadorSemantico
    def __init__(self):  # Método constructor de la clase
        self.palabras_clave = {  # Creación de un diccionario de palabras clave y sus significados
            'comer': 'acción de ingerir alimentos',  # Palabra clave y su significado
            'dormir': 'estado de reposo del organismo',  # Palabra clave y su significado
            'correr': 'moverse rápidamente con los pies',  # Palabra clave y su significado
            'felicidad': 'estado emocional positivo',  # Palabra clave y su significado
            'tristeza': 'estado emocional negativo'  # Palabra clave y su significado
        }

    def analizar_oracion(self, oracion):  # Método para analizar una oración
        palabras_encontradas = []  # Lista para almacenar las palabras clave encontradas

        for palabra in oracion.split():  # Iteración sobre cada palabra en la oración
            if palabra.lower() in self.palabras_clave:  # Verifica si la palabra está en el diccionario de palabras clave
                palabras_encontradas.append((palabra, self.palabras_clave[palabra.lower()]))  # Agrega la palabra y su significado a la lista de resultados

        return palabras_encontradas  # Retorna la lista de palabras clave encontradas junto con sus significados

# Ejemplo de uso
analizador = AnalizadorSemantico()  # Instancia del analizador semántico
oracion = "Me gusta correr por la mañana porque me da felicidad."  # Oración de ejemplo
resultado_analisis = analizador.analizar_oracion(oracion)  # Realiza el análisis semántico de la oración

print("Análisis Semántico:")  # Imprime un mensaje indicando el análisis semántico
for palabra, significado in resultado_analisis:  # Iteración sobre las palabras clave encontradas y sus significados
    print(f"Palabra clave: {palabra}, Significado: {significado}")  # Imprime la palabra clave y su significado
