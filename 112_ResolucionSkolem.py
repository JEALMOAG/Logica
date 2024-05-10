"""
Created on 18 April  01:19:14 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
Este código utiliza la biblioteca `sympy` para trabajar con lógica proposicional.
 Define símbolos lógicos, crea cláusulas con ellos, y luego convierte estas
 cláusulas a Forma Normal Conjuntiva (CNF). Finalmente, verifica si la fórmula 
 CNF es satisfacible o no, e imprime un mensaje en consecuencia.
'''
from sympy import symbols, Not, Or, And, Implies, satisfiable
from sympy.logic.boolalg import to_cnf

# Define los símbolos lógicos
A, B = symbols('A B')

# Define las cláusulas
clauses = [
    Or(A, B),  # Cláusula A OR B
    Or(A),     # Cláusula A
    Or(B)      # Cláusula B
]

# Convierte a Forma Normal Conjuntiva (CNF)
cnf = to_cnf(And(*clauses))

# Muestra la Forma Normal Conjuntiva
print("Forma Normal Conjuntiva (CNF):", cnf)

# Comprueba la satisfacibilidad
if satisfiable(cnf):
    print("La fórmula es satisfacible.")  # Si la fórmula es satisfacible, imprime este mensaje
else:
    print("La fórmula no es satisfacible.")  # Si la fórmula no es satisfacible, imprime este mensaje
