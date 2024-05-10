"""
created on 26 Abril 13:21:57 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código proporciona una función para realizar un análisis léxico en una cadena
de entrada de código. Divide la cadena en tokens, que pueden ser palabras
reservadas, símbolos o identificadores. Luego, devuelve una lista de tokens con
sus respectivos tipos. Además, incluye un ejemplo de uso que demuestra cómo
analizar una cadena de código y mostrar los tokens encontrados junto con sus
tipos correspondientes.
"""
# Definición de palabras clave y símbolos
palabras_reservadas = {'if', 'else', 'while', 'for', 'int', 'float', 'return'}  # Conjunto de palabras reservadas
simbolos = {'(', ')', '{', '}', ';', ',', '+', '-', '*', '/'}  # Conjunto de símbolos

# Función para realizar el análisis léxico
def analisis_lexico(cadena):
    tokens = []  # Lista para almacenar los tokens encontrados
    palabra_actual = ''  # Variable para almacenar la palabra actual

    # Itera sobre cada caracter en la cadena
    for caracter in cadena:
        # Si el caracter es un espacio en blanco, verifica si hay una palabra actual
        if caracter.isspace():
            if palabra_actual:
                # Si la palabra actual es una palabra reservada, agrégala como token
                if palabra_actual in palabras_reservadas:
                    tokens.append(('PALABRA_RESERVADA', palabra_actual))
                else:
                    # De lo contrario, agrégala como identificador
                    tokens.append(('IDENTIFICADOR', palabra_actual))
                palabra_actual = ''  # Restablece la palabra actual
        # Si el caracter es un símbolo, verifica si hay una palabra actual
        elif caracter in simbolos:
            if palabra_actual:
                # Si hay una palabra actual, agrégala como identificador
                tokens.append(('IDENTIFICADOR', palabra_actual))
                palabra_actual = ''  # Restablece la palabra actual
            # Agrega el símbolo como token
            tokens.append(('SIMBOLO', caracter))
        else:
            # Agrega el caracter a la palabra actual
            palabra_actual += caracter
    
    # Verifica si hay una palabra actual después del bucle
    if palabra_actual:
        # Si la palabra actual es una palabra reservada, agrégala como token
        if palabra_actual in palabras_reservadas:
            tokens.append(('PALABRA_RESERVADA', palabra_actual))
        else:
            # De lo contrario, agrégala como identificador
            tokens.append(('IDENTIFICADOR', palabra_actual))

    return tokens

# Ejemplo de uso
entrada = "if (x > 0) { return x; } else { return -x; }"
tokens = analisis_lexico(entrada)
for token in tokens:
    print(token)
