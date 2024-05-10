"""
created on 26 Abril 09:35:05 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código implementa un analizador léxico en Python utilizando expresiones
regulares. Define tokens con patrones de expresiones regulares y luego analiza
una cadena de entrada buscando coincidencias con estos patrones. Si encuentra
una coincidencia, agrega el tipo y el valor del token a una lista de resultados.
Si no encuentra una coincidencia, muestra un mensaje de error.
"""
import re  # Importa el módulo 're' para utilizar expresiones regulares

# Definición de tokens utilizando expresiones regulares
tokens = [
    ('ENTERO', r'\d+'),          # Token para números enteros
    ('SUMA', r'\+'),             # Token para el operador de suma
    ('RESTA', r'\-'),            # Token para el operador de resta
    ('MULTIPLICACION', r'\*'),   # Token para el operador de multiplicación
    ('DIVISION', r'\/'),         # Token para el operador de división
    ('ESPACIO_BLANCO', r'\s+'),  # Token para espacio en blanco
]

# Función para realizar el análisis léxico
def analisis_lexico(cadena):
    indice = 0            # Inicializa el índice de la cadena
    resultado = []        # Inicializa una lista para almacenar los tokens
    while indice < len(cadena):  # Itera sobre cada carácter de la cadena
        coincidencia = None      # Inicializa la variable para almacenar la coincidencia
        for token in tokens:    # Itera sobre cada token definido
            tipo, patron = token  # Obtiene el tipo y el patrón de la expresión regular del token
            regex = re.compile(patron)  # Compila el patrón en una expresión regular
            coincidencia = regex.match(cadena, indice)  # Intenta encontrar una coincidencia desde el índice actual
            if coincidencia:    # Si hay una coincidencia
                valor = coincidencia.group(0)  # Obtiene el valor coincidente
                if tipo != 'ESPACIO_BLANCO':  # Si el token no es un espacio en blanco
                    resultado.append((tipo, valor))  # Agrega el tipo y el valor a la lista de resultados
                break  # Sale del bucle de tokens
        if not coincidencia:  # Si no se encuentra ninguna coincidencia
            print("Caracter no reconocido:", cadena[indice])  # Imprime un mensaje de error
            break  # Sale del bucle de caracteres
        else:  # Si se encontró una coincidencia
            indice = coincidencia.end()  # Actualiza el índice al final de la coincidencia encontrada
    return resultado  # Devuelve la lista de tokens encontrados

# Ejemplo de uso
entrada = "3 + 4 * 2"  # Define una cadena de entrada
resultado = analisis_lexico(entrada)  # Realiza el análisis léxico de la cadena
print(resultado)  # Imprime los tokens encontrados
