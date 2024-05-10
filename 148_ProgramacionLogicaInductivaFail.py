"""
created on 25 Abril 16:52:39 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código presenta una implementación simplificada del algoritmo FOIL
(First Order Inductive Learner), que es un algoritmo de aprendizaje inductivo
utilizado para inducir reglas de clasificación a partir de ejemplos de entrenamiento.
El algoritmo busca encontrar la cláusula más específica y la cláusula más
general que describen los ejemplos positivos y negativos, respectivamente.
Luego, utiliza estas cláusulas para predecir la clase de nuevos ejemplos.
"""
class ReglaFOIL:  # Definición de la clase ReglaFOIL
    def __init__(self, predicado_objetivo, conocimiento_previo):  # Método constructor que recibe el predicado objetivo y el conocimiento previo
        self.predicado_objetivo = predicado_objetivo  # Predicado objetivo (clase)
        self.conocimiento_previo = conocimiento_previo  # Conocimiento previo

    def entrenar(self, ejemplos):  # Método para entrenar el modelo, recibe ejemplos de entrenamiento
        # Encuentra la cláusula más específica
        self.clausula_especifica = self.encontrar_clausula_especifica(ejemplos)

        # Encuentra la cláusula más general
        self.clausula_general = self.encontrar_clausula_general(ejemplos)

    def encontrar_clausula_especifica(self, ejemplos):  # Método para encontrar la cláusula más específica, recibe ejemplos de entrenamiento
        clausula_especifica = []  # Inicialización de la lista de la cláusula específica

        for ejemplo in ejemplos:  # Itera sobre los ejemplos
            if ejemplo[1] == 'Yes':  # Si el ejemplo pertenece a la clase positiva
                clausula_especifica.append(ejemplo[0])  # Agrega las características a la cláusula específica

        return clausula_especifica  # Devuelve la cláusula específica

    def encontrar_clausula_general(self, ejemplos):  # Método para encontrar la cláusula más general, recibe ejemplos de entrenamiento
        clausula_general = []  # Inicialización de la lista de la cláusula general

        for ejemplo in ejemplos:  # Itera sobre los ejemplos
            if ejemplo[1] == 'No':  # Si el ejemplo no pertenece a la clase positiva
                clausula_general.append(ejemplo[0])  # Agrega las características a la cláusula general

        return clausula_general  # Devuelve la cláusula general

    def predecir(self, ejemplo):  # Método para predecir la clase de un ejemplo dado
        # Comprueba si el ejemplo satisface la cláusula específica
        for termino in self.clausula_especifica:  # Itera sobre los términos de la cláusula específica
            if termino not in ejemplo[0]:  # Si un término no está presente en el ejemplo
                return 'No'  # Devuelve 'No'

        # Comprueba si el ejemplo no satisface la cláusula general
        for termino in self.clausula_general:  # Itera sobre los términos de la cláusula general
            if termino in ejemplo[0]:  # Si un término está presente en el ejemplo
                return 'No'  # Devuelve 'No'

        return 'Yes'  # Si no se cumple ninguna de las condiciones anteriores, devuelve 'Yes'

# Datos de ejemplo (Formato: (Características, Clase))
ejemplos = [  # Definición de ejemplos de entrenamiento
    (['nublado', 'frío', 'normal'], 'No'),  # Ejemplo 1
    (['soleado', 'calor', 'alta'], 'Yes'),  # Ejemplo 2
    (['nublado', 'calor', 'normal'], 'Yes'),  # Ejemplo 3
    (['lluvia', 'frío', 'normal'], 'No'),  # Ejemplo 4
    (['soleado', 'templado', 'alta'], 'Yes')  # Ejemplo 5
]

# Definición del predicado objetivo y el conocimiento previo
predicado_objetivo = 'Jugar'  # Predicado objetivo
conocimiento_previo = []  # Conocimiento previo (vacío en este caso)

# Entrenamiento del modelo FOIL
foil = ReglaFOIL(predicado_objetivo, conocimiento_previo)  # Creación de una instancia de ReglaFOIL
foil.entrenar(ejemplos)  # Entrenamiento del modelo con los ejemplos

# Predicción para un nuevo ejemplo
nuevo_ejemplo = (['soleado', 'frio', 'normal'], 'Desconocido')  # Definición de un ejemplo desconocido
prediccion = foil.predecir(nuevo_ejemplo)  # Predicción de la clase del nuevo ejemplo
print("Predicción para el ejemplo:", prediccion)  # Impresión de la predicción
