"""
created on 25 Abril 13:45:29 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código implementa Aprendizaje Inductivo utilizando reglas. Define una clase
Regla para representar reglas con condiciones y una clase asociada, y una clase
AprendizajeInductivo para entrenar un modelo y explicar predicciones utilizando
estas reglas. Utiliza datos meteorológicos para ilustrar el entrenamiento del
modelo y la explicación de predicciones basadas en las reglas aprendidas.
"""
class Regla:
    def __init__(self, condiciones, clase):
        # Inicializa la regla con las condiciones y la clase asociada
        self.condiciones = condiciones  # Condiciones de la regla
        self.clase = clase  # Clase asociada a la regla

    def cubre(self, instancia):
        # Verifica si la regla cubre la instancia
        for i, condicion in enumerate(self.condiciones):
            # Compara cada condición de la regla con la instancia actual
            if condicion != instancia[i] and condicion != '?':
                # Si la condición no coincide con la instancia y no es un valor de "don't care" ('?'), la regla no cubre la instancia
                return False
        # Si todas las condiciones coinciden (o son "don't care"), la regla cubre la instancia
        return True

# Definición de la clase AprendizajeInductivo
class AprendizajeInductivo:
    def __init__(self, caracteristicas, objetivo):
        # Inicializa el AprendizajeInductivo con las características y la variable objetivo
        self.caracteristicas = caracteristicas  # Características
        self.objetivo = objetivo  # Variable objetivo
        self.reglas = []  # Lista de reglas

    def entrenar(self, instancias):
        # Entrena el modelo generando reglas para cada instancia
        for instancia in instancias:
            # Crea una regla con las características de la instancia y la clase asociada
            regla = Regla(instancia[:-1], instancia[-1])
            # Agrega la regla a la lista de reglas
            self.reglas.append(regla)

    def explicar(self, instancia):
        # Explica la predicción para una instancia dada utilizando las reglas generadas
        explicaciones = []
        for regla in self.reglas:
            if regla.cubre(instancia):
                # Si una regla cubre la instancia, agrega la regla y su clase asociada a las explicaciones
                explicacion = {
                    'regla': regla.condiciones,
                    'clase': regla.clase
                }
                explicaciones.append(explicacion)
        return explicaciones

# Datos de ejemplo
instancias = [
    ['Nublado', 'Frio', 'Alto', 'No'],
    ['Soleado', 'Calor', 'Normal', 'Si'],
    ['Nublado', 'Calor', 'Alto', 'Si'],
    ['Lluvia', 'Frio', 'Normal', 'No'],
    ['Soleado', 'Templado', 'Alto', 'Si']
]

# Entrenamiento del modelo
ai = AprendizajeInductivo(caracteristicas=['Tiempo', 'Temperatura', 'Humedad'], objetivo='Jugar')
ai.entrenar(instancias)

# Explicaciones e información relevante para nuevas instancias
nueva_instancia = ['Soleado', 'Frio', 'Alto']
explicaciones = ai.explicar(nueva_instancia)
print("Explicaciones para la instancia", nueva_instancia)
for explicacion in explicaciones:
    print("Regla:", explicacion['regla'], "Clase:", explicacion['clase'])
