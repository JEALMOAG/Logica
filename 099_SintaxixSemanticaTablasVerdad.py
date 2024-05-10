"""
created on 13 Abril 16:27:09 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código proporciona una función llamada generar_tabla_verdad que toma una
expresión proposicional como entrada y genera su tabla de verdad correspondiente.
Primero, identifica las variables en la expresión, luego genera todas las
combinaciones posibles de valores de verdad para estas variables y evalúa la
expresión en cada combinación. Finalmente, imprime la tabla de verdad con los
resultados de estas evaluaciones. El código es capaz de manejar expresiones con
variables y operadores lógicos como AND, OR, y NOT.
"""
import itertools  # Importa el módulo itertools para trabajar con iteradores y combinaciones.

def generar_tabla_verdad(expresion):  # Define una función llamada generar_tabla_verdad que toma una expresión proposicional como argumento.
    variables = sorted(set(c for c in expresion if c.isalpha()))  # Encuentra todas las letras únicas en la expresión y las ordena alfabéticamente.
    num_vars = len(variables)  # Calcula la cantidad de variables en la expresión.
    filas = list(itertools.product([False, True], repeat=num_vars))  # Genera todas las combinaciones de valores de verdad para las variables.

    print("Tabla de Verdad para la expresión:", expresion)  # Imprime un encabezado para la tabla de verdad.
    print("-" * (4 * num_vars + 3))  # Imprime una línea divisoria.
    print("|", end="")  # Imprime el inicio de la fila de encabezados de variables.
    for var in variables:  # Itera sobre las variables.
        print(f" {var} |", end="")  # Imprime el nombre de cada variable.
    print(f" {expresion} |")  # Imprime el nombre de la expresión al final de la fila.
    print("-" * (4 * num_vars + 3))  # Imprime otra línea divisoria.

    for fila in filas:  # Itera sobre todas las filas de la tabla de verdad.
        fila_eval = {var: val for var, val in zip(variables, fila)}  # Crea un diccionario con los valores de verdad de las variables en esta fila.
        resultado = eval(expresion, fila_eval)  # Evalúa la expresión proposicional en esta fila.
        print("|", end="")  # Imprime el inicio de la fila.
        for val in fila:  # Itera sobre los valores de verdad de las variables en esta fila.
            print(f" {val} |", end="")  # Imprime cada valor de verdad.
        print(f" {resultado} |")  # Imprime el resultado de evaluar la expresión en esta fila.
        print("-" * (4 * num_vars + 3))  # Imprime otra línea divisoria al final de la fila.

# Ejemplo de uso
if __name__ == "__main__":  # Verifica si el script está siendo ejecutado directamente.
    expresion = '(p & q) | (~p)'  # Define una expresión proposicional de ejemplo.
    #input("Ingrese una expresión proposicional usando solo letras y los operadores lógicos (& para AND, | para OR, ~ para NOT, > para IMPLICA, y = para EQUIVALENCIA): ")
    generar_tabla_verdad(expresion)  # Genera la tabla de verdad para la expresión dada.
