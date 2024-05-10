"""
created on 24 Abril 18:56:23 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
Este código utiliza el conjunto de datos Iris para entrenar un clasificador
de árbol de decisión y luego evalúa su precisión en un conjunto de prueba.
Primero, carga los datos de Iris y los divide en conjuntos de entrenamiento
y prueba. Luego, crea un clasificador de árbol de decisión y lo entrena con
los datos de entrenamiento. Posteriormente, realiza predicciones sobre el
conjunto de prueba y calcula la precisión comparando las etiquetas verdaderas
con las predichas. Finalmente, imprime la precisión del clasificador.
"""
from sklearn.datasets import load_iris  # Importamos la función load_iris desde sklearn.datasets
from sklearn.model_selection import train_test_split  # Importamos la función train_test_split desde sklearn.model_selection
from sklearn.tree import DecisionTreeClassifier  # Importamos la clase DecisionTreeClassifier desde sklearn.tree
from sklearn.metrics import accuracy_score  # Importamos la función accuracy_score desde sklearn.metrics

# Cargar el conjunto de datos Iris
iris_datos = load_iris()  # Cargar el conjunto de datos Iris
X_caracteristicas = iris_datos.data  # Obtener las características de los datos
y_etiquetas = iris_datos.target  # Obtener las etiquetas de los datos

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X_caracteristicas, y_etiquetas, test_size=0.2, random_state=42)  # Dividir los datos en conjuntos de entrenamiento y prueba

# Crear un clasificador de árbol de decisión K-DT
arbol_decision_k = DecisionTreeClassifier()  # Crear un clasificador de árbol de decisión

# Entrenar el clasificador
arbol_decision_k.fit(X_entrenamiento, y_entrenamiento)  # Entrenar el clasificador con los datos de entrenamiento

# Realizar predicciones en el conjunto de prueba
y_predicciones = arbol_decision_k.predict(X_prueba)  # Realizar predicciones sobre los datos de prueba

# Calcular la precisión
precision = accuracy_score(y_prueba, y_predicciones)  # Calcular la precisión comparando las etiquetas verdaderas con las predichas
print("Precisión del clasificador K-DT:", precision)  # Imprimir la precisión obtenida
