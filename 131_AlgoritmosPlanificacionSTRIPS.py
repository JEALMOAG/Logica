"""
created on 22 Abril 10:45:18 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código presenta una implementación de un planificador de tareas basado en el
algoritmo STRIPS. Define una clase Actividad que representa una acción con
precondiciones y efectos, y una clase PlanificadorTareas que planifica una
secuencia de actividades para pasar de un estado inicial a un estado objetivo.
El planificador selecciona y ejecuta acciones aplicables hasta alcanzar el
objetivo, mostrando el plan resultante si es alcanzable.
"""
class Actividad:
    def __init__(self, nombre, requisitos, consecuencias):
        self.nombre = nombre  # Nombre de la actividad
        self.requisitos = requisitos  # Requisitos necesarios para que la actividad sea aplicable
        self.consecuencias = consecuencias  # Consecuencias que tiene la actividad sobre el estado

    def es_aplicable(self, situacion):
        # Comprueba si los requisitos de la actividad son satisfechos por la situación actual
        return all(item in situacion.items() for item in self.requisitos.items())

    def aplicar(self, situacion):
        if self.es_aplicable(situacion):
            # Aplica las consecuencias de la actividad a la situación actual si es aplicable
            nueva_situacion = situacion.copy()
            nueva_situacion.update(self.consecuencias)
            return nueva_situacion
        else:
            return None

class PlanificadorTareas:
    def __init__(self, situacion_inicial, situacion_objetivo, actividades):
        self.situacion_inicial = situacion_inicial  # Situación inicial del problema
        self.situacion_objetivo = situacion_objetivo  # Situación que se quiere alcanzar (objetivo)
        self.actividades = actividades  # Lista de actividades disponibles

    def planificar(self):
        plan = []  # Lista que contendrá las actividades del plan
        situacion_actual = self.situacion_inicial.copy()  # Situación actual del problema

        while not self.satisface(situacion_actual, self.situacion_objetivo):
            # Mientras la situación actual no satisfaga la situación objetivo:
            actividades_aplicables = [actividad for actividad in self.actividades if actividad.es_aplicable(situacion_actual)]
            # Encuentra las actividades aplicables en la situación actual
            if not actividades_aplicables:
                print("No se puede alcanzar la situación objetivo desde la situación inicial.")
                return None
            actividad_elegida = actividades_aplicables[0]  # Escoge la primera actividad aplicable
            plan.append(actividad_elegida)  # Añade la actividad al plan
            situacion_actual = actividad_elegida.aplicar(situacion_actual)  # Aplica la actividad a la situación actual

        return plan

    def satisface(self, situacion, situacion_objetivo):
        # Comprueba si la situación actual satisface la situación objetivo
        return all(item in situacion.items() for item in situacion_objetivo.items())

# Definir la situación inicial
situacion_inicial = {"en_casa": True, "tiene_llave": False}

# Definir la situación objetivo
situacion_objetivo = {"en_escuela": True, "tiene_llave": True}

# Definir las actividades disponibles
actividades = [
    Actividad("ir_a_escuela", {"en_casa": True, "tiene_llave": True}, {"en_casa": False, "en_escuela": True}),
    Actividad("tomar_llave", {"en_casa": True, "tiene_llave": False}, {"tiene_llave": True})
]

# Crear el planificador
planificador = PlanificadorTareas(situacion_inicial, situacion_objetivo, actividades)

# Obtener el plan
plan = planificador.planificar()

# Imprimir el plan
if plan:
    print("Plan encontrado:")
    for actividad in plan:
        print(actividad.nombre)
