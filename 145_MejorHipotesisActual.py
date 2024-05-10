"""
created on 25 Abril 08:28:04 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código define una clase llamada MejorHipotesisActual que implementa un
algoritmo de aprendizaje basado en el algoritmo de la "Mejor Hipótesis Actual"
para clasificación de datos discretos. Esta clase tiene métodos para entrenar
el modelo y hacer predicciones. Además, proporciona un ejemplo de uso con
datos de entrenamiento y una nueva instancia para predecir su clase.
"""
class MejorHipotesisActual:
    def __init__(self, caracteristicas, objetivo):
        # Inicialización de la clase con características y variable objetivo
        self.caracteristicas = caracteristicas  # Lista de características
        self.objetivo = objetivo      # Nombre de la variable objetivo
        self.hipotesis = None    # Hipótesis inicialmente vacía

    def entrenar(self, instancias):
        # Método para entrenar el modelo
        self.hipotesis = {}  # Diccionario para almacenar la hipótesis
        for i, val in enumerate(self.caracteristicas):
            # Encuentra el valor más frecuente para cada característica
            self.hipotesis[val] = self.encontrar_valor_mas_frecuente(instancias, i)

    def encontrar_valor_mas_frecuente(self, instancias, indice):
        # Encuentra el valor más frecuente en una columna específica
        valores = [instancia[indice] for instancia in instancias]
        return max(set(valores), key=valores.count)

    def predecir(self, instancia):
        # Método para predecir la clase de una nueva instancia
        if self.hipotesis is None:
            raise Exception("El modelo no ha sido entrenado todavía.")
        prediccion = self.hipotesis[self.caracteristicas[0]]  # Predicción inicial
        for i, val in enumerate(self.caracteristicas):
            # Compara cada característica de la instancia con la hipótesis
            if instancia[i] != self.hipotesis[val]:
                return prediccion  # Retorna la predicción actual
        return prediccion  # Retorna la predicción final


# Ejemplo de uso
if __name__ == "__main__":
    # Datos de ejemplo (características discretas)
    caracteristicas = ['F1', 'F2', 'F3']  # Lista de características
    objetivo = 'Clase'               # Variable objetivo
    instancias = [                  # Instancias de entrenamiento
        ['A', 'X', 'Y', 'Positivo'],
        ['B', 'X', 'Y', 'Positivo'],
        ['A', 'Z', 'Y', 'Negativo'],
        ['B', 'Z', 'X', 'Negativo'],
        ['A', 'X', 'X', 'Positivo']
    ]

    # Entrenamiento del modelo
    mha = MejorHipotesisActual(caracteristicas, objetivo)
    mha.entrenar(instancias)

    # Predicción de nuevas instancias
    nueva_instancia = ['B', 'X', 'X']   # Nueva instancia
    prediccion = mha.predecir(nueva_instancia)  # Predicción
    print("Predicción:", prediccion)  # Imprime la predicción
