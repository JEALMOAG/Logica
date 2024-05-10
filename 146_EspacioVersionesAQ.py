"""
created on 25 Abril 13:45:29 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código define dos clases: "EspacioVersiones" y "AQ".
"EspacioVersiones" gestiona la generalización y especialización de hipótesis
basadas en instancias.
"AQ" implementa el algoritmo AQ para aprendizaje inductivo desde ejemplos,
generalizando si la etiqueta es 'Positivo' y especializando si es 'Negativo'.
Luego, realiza predicciones utilizando la hipótesis aprendida.
"""
class EspacioVersiones:
    def __init__(self, num_caracteristicas):
        # Inicializa el objeto EspacioVersiones con el número de características especificado
        self.num_caracteristicas = num_caracteristicas
        # Inicializa la hipótesis con una lista de longitud num_caracteristicas, con todos los elementos como '0'
        self.hipotesis = ['0'] * num_caracteristicas

    def generalizar(self, instancia):
        # Generaliza la hipótesis basada en una instancia dada
        for i, valor in enumerate(instancia):
            if self.hipotesis[i] != valor:
                self.hipotesis[i] = '?'

    def especializar(self, instancia):
        # Especializa la hipótesis basada en una instancia dada
        for i, valor in enumerate(instancia):
            if self.hipotesis[i] == '?':
                self.hipotesis[i] = valor

    def predecir(self, instancia):
        # Predice la clase de una instancia dada utilizando la hipótesis actual
        for i, valor in enumerate(instancia):
            if self.hipotesis[i] != '?' and self.hipotesis[i] != valor:
                return 'No se puede clasificar'
        return 'Positivo'

class AQ:
    def __init__(self, num_caracteristicas):
        # Inicializa el objeto AQ con una hipótesis inicial creada utilizando EspacioVersiones
        self.hipotesis = EspacioVersiones(num_caracteristicas)

    def entrenar(self, instancias):
        # Entrena el modelo AQ utilizando instancias etiquetadas
        for instancia in instancias:
            if instancia[-1] == 'Positivo':
                # Generaliza si la etiqueta es 'Positivo'
                self.hipotesis.generalizar(instancia[:-1])
            else:
                # Especializa si la etiqueta es 'Negativo'
                self.hipotesis.especializar(instancia[:-1])

    def predecir(self, instancia):
        # Predice la clase de una instancia dada utilizando la hipótesis aprendida
        return self.hipotesis.predecir(instancia)

# Datos de ejemplo
instancias = [
    ['1', '1', 'Positivo'],
    ['0', '0', 'Negativo'],
    ['0', '1', 'Negativo'],
    ['1', '0', 'Positivo']
]

# Entrenamiento del modelo
aq = AQ(num_caracteristicas=2)
aq.entrenar(instancias)

# Predicción de nuevas instancias
nuevas_instancias = [
    ['1', '1'],
    ['0', '1'],
    ['1', '0'],
    ['0', '0']
]

for instancia in nuevas_instancias:
    # Realiza predicciones para cada nueva instancia y muestra el resultado
    prediccion = aq.predecir(instancia)
    print("Instancia:", instancia, "Predicción:", prediccion)
