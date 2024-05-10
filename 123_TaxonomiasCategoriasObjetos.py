"""
Created on 19 April  14:19:17 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
Este código implementa una jerarquía de categorías y subcategorías, donde cada
 categoría puede tener una relación de padre-hijo con otra categoría. Se pueden
 agregar categorías y subcategorías a la jerarquía, y también se pueden consultar
 las subcategorías de una categoría específica.
'''
class Jerarquia:
    def __init__(self):
        # Inicializa la jerarquía como un diccionario vacío
        self.categorias = {}

    def agregar_categoria(self, categoria, padre=None):
        # Agrega una categoría al diccionario de la jerarquía
        if categoria not in self.categorias:
            self.categorias[categoria] = set()  # Si la categoría no existe, crea un conjunto vacío para sus subcategorías
        if padre:  # Si se proporciona un padre, añade este a la lista de subcategorías
            if padre not in self.categorias:
                self.categorias[padre] = set()  # Si el padre no existe, crea un conjunto vacío para sus subcategorías
            self.categorias[padre].add(categoria)  # Agrega la categoría como subcategoría del padre

    def obtener_subcategorias(self, categoria):
        # Obtiene las subcategorías de una categoría dada
        if categoria in self.categorias:
            return self.categorias[categoria]  # Devuelve el conjunto de subcategorías
        else:
            return set()  # Devuelve un conjunto vacío si la categoría no tiene subcategorías

# Crear una instancia de la jerarquía
jerarquia = Jerarquia()

# Agregar categorías y subcategorías
jerarquia.agregar_categoria("Alimento")
jerarquia.agregar_categoria("Fruta", padre="Alimento")
jerarquia.agregar_categoria("Vegetal", padre="Alimento")
jerarquia.agregar_categoria("Manzana", padre="Fruta")
jerarquia.agregar_categoria("Pera", padre="Fruta")
jerarquia.agregar_categoria("Zanahoria", padre="Vegetal")

# Consultar subcategorías
print("Subcategorías de Alimento:", jerarquia.obtener_subcategorias("Alimento"))
print("Subcategorías de Fruta:", jerarquia.obtener_subcategorias("Fruta"))
print("Subcategorías de Vegetal:", jerarquia.obtener_subcategorias("Vegetal"))
