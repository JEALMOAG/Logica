"""
Created on 18 April  00:29:19 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
Este código define una clase `Person` que representa a una persona con un 
nombre y una lista de padres. Cada persona puede tener una lista de padres 
asociada. El programa principal crea dos instancias de `Person`, "John" y "Mary",
 y asigna a "Mary" como padre de "John". Luego, verifica si cada persona tiene 
 padres o no e imprime un mensaje en consecuencia. El programa muestra cómo se
 pueden utilizar clases y métodos para modelar relaciones entre entidades, en 
 este caso, las personas y sus padres.
'''
class Person:  # Definición de la clase Person
    def __init__(self, name):  # Constructor de la clase Person
        self.name = name  # Asignación del atributo name
        self.parents = []  # Inicialización de la lista de padres

    def add_parent(self, parent):  # Método para agregar padres
        self.parents.append(parent)  # Agregar padre a la lista de padres

    def __str__(self):  # Método especial para convertir a cadena
        return self.name  # Devuelve el nombre de la persona como cadena

def main():  # Función principal
    john = Person("John")  # Crear una instancia de Person llamada John
    mary = Person("Mary")  # Crear una instancia de Person llamada Mary

    john.add_parent(mary)  # Asignar a Mary como padre de John

    # Inferencia simple
    for person in [john, mary]:  # Iterar sobre las instancias de Person
        if len(person.parents) > 0:  # Comprobar si la persona tiene padres
            print(f"{person} has parents.")  # Imprimir si tiene padres
        else:
            print(f"{person} doesn't have parents.")  # Imprimir si no tiene padres

if __name__ == "__main__":  # Entrada principal del programa
    main()  # Llamar a la función principal si se ejecuta como script




