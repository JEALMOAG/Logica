"""
created on 24 Abril 21:41:01 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código implementa un clasificador K-Vecinos más Cercanos (K-NN) con
Distancia Euclidiana (K-DL) desde cero utilizando NumPy. Entrena el modelo con
datos de entrenamiento y realiza predicciones en un conjunto de prueba.
Calcula distancias euclidianas entre las muestras de prueba y entrenamiento,
encuentra las k muestras más cercanas, y predice la etiqueta más frecuente
como la etiqueta de la muestra actual. Finalmente, calcula la precisión del
clasificador comparando las etiquetas verdaderas con las predichas en el
conjunto de prueba.
"""
import numpy as np

class ClasificadorKDL:
    def __init__(self, k):
        self.k = k

    def ajustar(self, X_entrenamiento, y_entrenamiento):
        # Almacenar los datos de entrenamiento
        self.X_entrenamiento = X_entrenamiento
        self.y_entrenamiento = y_entrenamiento

    def predecir(self, X_prueba):
        # Inicializar una lista para almacenar las predicciones
        y_pred = []
        # Iterar sobre cada muestra en el conjunto de datos de prueba
        for muestra in X_prueba:
            # Calcular las distancias euclidianas entre la muestra actual y todas las muestras de entrenamiento
            distancias = np.sqrt(np.sum((self.X_entrenamiento - muestra) ** 2, axis=1))
            # Encontrar los índices de las k muestras más cercanas
            k_indices_mas_cercanos = np.argsort(distancias)[:self.k]
            # Obtener las etiquetas correspondientes a las k muestras más cercanas
            etiquetas_mas_cercanas = self.y_entrenamiento[k_indices_mas_cercanos]
            # Contar las ocurrencias de cada etiqueta
            etiquetas_unicas, cuentas = np.unique(etiquetas_mas_cercanas, return_counts=True)
            # Predecir la etiqueta más frecuente como la etiqueta de la muestra actual
            etiqueta_predicha = etiquetas_unicas[np.argmax(cuentas)]
            # Agregar la etiqueta predicha a la lista de predicciones
            y_pred.append(etiqueta_predicha)
        # Convertir la lista de predicciones en un array NumPy y devolverlo
        return np.array(y_pred)

# Ejemplo de uso
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el clasificador K-DL
clasificador_kdl = ClasificadorKDL(k=5)
clasificador_kdl.ajustar(X_entrenamiento, y_entrenamiento)

# Realizar predicciones en el conjunto de prueba
y_pred = clasificador_kdl.predecir(X_prueba)

# Calcular la precisión del clasificador
precision = accuracy_score(y_prueba, y_pred)
print("Precisión del clasificador K-DL:", precision)
