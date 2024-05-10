"""
created on 25 Abril 22:35:43 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código implementa una clase llamada GramaticaRegular que permite generar
cadenas aleatorias y verificar si una cadena dada es válida en una gramática
regular. Utiliza producciones gramaticales para generar cadenas y realiza un
análisis de pila para verificar la validez de una cadena. Además, proporciona
un ejemplo de uso que demuestra cómo crear una gramática regular, generar cadenas
aleatorias y verificar la validez de una cadena específica.
"""
import re  # Importa el módulo de expresiones regulares
import random  # Importa el módulo de generación de números aleatorios

class GramaticaRegular:  # Definición de la clase GramaticaRegular
    def __init__(self, producciones):  # Método constructor que recibe las producciones de la gramática
        self.producciones = producciones  # Inicialización de las producciones de la gramática

    def generar_cadena_aleatoria(self, simbolo_inicial, longitud_maxima=10):  # Método para generar una cadena aleatoria
        cadena = ""  # Inicialización de la cadena
        simbolo_actual = simbolo_inicial  # Símbolo inicial

        while len(cadena) < longitud_maxima:  # Bucle mientras la longitud de la cadena sea menor que la longitud máxima
            if simbolo_actual not in self.producciones:  # Si el símbolo actual no tiene producciones
                break  # Salir del bucle
            produccion = random.choice(self.producciones[simbolo_actual])  # Selecciona una producción aleatoria para el símbolo actual
            cadena += produccion[1]  # Agrega el símbolo terminal de la producción a la cadena
            simbolo_actual = produccion[0]  # Actualiza el símbolo actual al siguiente símbolo no terminal de la producción

        return cadena  # Devuelve la cadena generada

    def es_valida(self, cadena, simbolo_inicial):  # Método para verificar si una cadena es válida en la gramática
        pila = [(simbolo_inicial, 0)]  # Inicialización de la pila con el símbolo inicial y el índice 0

        while pila:  # Bucle mientras la pila no esté vacía
            simbolo, indice = pila.pop()  # Desapila un símbolo y su índice
            if indice == len(cadena):  # Si el índice es igual a la longitud de la cadena
                if simbolo == simbolo_inicial:  # Si el símbolo es el inicial
                    return True  # La cadena es válida
                continue  # Continuar con el siguiente símbolo de la pila

            if simbolo in self.producciones:  # Si el símbolo está en las producciones
                producciones = self.producciones[simbolo]  # Obtiene las producciones del símbolo
                for produccion in producciones:  # Itera sobre las producciones
                    if cadena[indice:].startswith(produccion[1]):  # Si la cadena desde el índice coincide con el símbolo terminal de la producción
                        for caracter in reversed(produccion[0]):  # Agrega los símbolos no terminales de la producción a la pila en orden inverso
                            pila.append((caracter, indice))
                        pila.append((simbolo, indice + len(produccion[1])))  # Agrega el símbolo actual y actualiza el índice
                        break  # Sale del bucle de producción actual
                else:  # Si no se encontró una producción que coincida
                    continue  # Continuar con el siguiente símbolo de la pila
            elif simbolo == cadena[indice]:  # Si el símbolo es igual al carácter en la posición del índice
                pila.append((simbolo_inicial, indice + 1))  # Agrega el símbolo inicial y actualiza el índice

        return False  # La cadena no es válida si se sale del bucle sin devolver True

# Ejemplo de uso
producciones = {  # Producciones de la gramática
    'S': [('A', '0'), ('B', '1')],  # Producciones para el símbolo S
    'A': [('A', '0'), ('B', '1')],  # Producciones para el símbolo A
    'B': [('S', '1'), ('B', '0')]   # Producciones para el símbolo B
}

gramatica = GramaticaRegular(producciones)  # Instancia de la clase GramaticaRegular con las producciones dadas
print("Producciones de la gramática:")  # Imprime un encabezado
for simbolo, producciones in producciones.items():  # Itera sobre los símbolos y sus producciones
    print(f"{simbolo} -> {' | '.join([f'{x[0]}{x[1]}' for x in producciones])}")  # Imprime las producciones de cada símbolo

# Generar una cadena aleatoria
cadena_aleatoria = gramatica.generar_cadena_aleatoria('S')  # Genera una cadena aleatoria comenzando desde el símbolo S
print("\nCadena generada aleatoriamente:", cadena_aleatoria)  # Imprime la cadena generada aleatoriamente

# Comprobar si una cadena es válida
cadena_prueba = "001110"  # Cadena de prueba
if gramatica.es_valida(cadena_prueba, 'S'):  # Verifica si la cadena es válida en la gramática empezando desde el símbolo S
    print("\nLa cadena es válida.")  # Imprime un mensaje si la cadena es válida
else:
    print("\nLa cadena no es válida.")  # Imprime un mensaje si la cadena no es válida




