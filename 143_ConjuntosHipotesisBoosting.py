"""
created on 24 Abril 15:09:35 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código utiliza el algoritmo AdaBoost para clasificar el conjunto de datos
Iris. Comienza cargando los datos de Iris, dividiéndolos en conjuntos de
entrenamiento y prueba, y luego entrena un clasificador AdaBoost con los datos
de entrenamiento. Posteriormente, realiza predicciones sobre el conjunto de
prueba y calcula la precisión de las predicciones. Finalmente, imprime la
precisión obtenida. En resumen, el código muestra cómo usar AdaBoost para
clasificación y evaluar su rendimiento en el conjunto de datos Iris.
"""
import numpy as np  # Importamos la biblioteca NumPy y la renombramos como np
from sklearn.datasets import load_iris  # Importamos la función load_iris desde sklearn.datasets
from sklearn.model_selection import train_test_split  # Importamos la función train_test_split desde sklearn.model_selection
from sklearn.ensemble import AdaBoostClassifier  # Importamos la clase AdaBoostClassifier desde sklearn.ensemble
from sklearn.metrics import accuracy_score  # Importamos la función accuracy_score desde sklearn.metrics

# Cargamos el conjunto de datos Iris
iris = load_iris()  # Cargamos el conjunto de datos Iris
caracteristicas = iris.data  # Obtenemos las características de los datos
etiquetas = iris.target  # Obtenemos las etiquetas de los datos

# Dividimos el conjunto de datos en entrenamiento y prueba
caracteristicas_entrenamiento, caracteristicas_prueba, etiquetas_entrenamiento, etiquetas_prueba = train_test_split(caracteristicas, etiquetas, test_size=0.2, random_state=42)  # Dividimos los datos en conjuntos de entrenamiento y prueba

# Creamos el clasificador AdaBoost
n_estimadores = 50  # Número de clasificadores débiles en el conjunto
tasa_aprendizaje = 1.0  # Tasa de aprendizaje
clasificador_boosting = AdaBoostClassifier(n_estimators=n_estimadores,  # Creamos un clasificador AdaBoost con el número de estimadores especificado
                                         learning_rate=tasa_aprendizaje,  # Asignamos la tasa de aprendizaje especificada
                                         random_state=42)  # Fijamos la semilla aleatoria para reproducibilidad

# Entrenamos el clasificador
clasificador_boosting.fit(caracteristicas_entrenamiento, etiquetas_entrenamiento)  # Entrenamos el clasificador AdaBoost utilizando los datos de entrenamiento

# Realizamos predicciones en el conjunto de prueba
etiquetas_predichas = clasificador_boosting.predict(caracteristicas_prueba)  # Realizamos predicciones sobre los datos de prueba

# Calculamos la precisión
precision = accuracy_score(etiquetas_prueba, etiquetas_predichas)  # Calculamos la precisión comparando las etiquetas verdaderas con las predichas
print("Precisión:", precision)  # Imprimimos la precisión obtenida
