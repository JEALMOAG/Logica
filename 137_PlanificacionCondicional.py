"""
created on 23 Abril 10:49:03 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código implementa un sistema simple de entorno y acciones condicionales.
Define clases para representar acciones condicionales y un entorno en el que
se pueden aplicar estas acciones. Las acciones dependen de condiciones
específicas en el entorno. El ejemplo muestra cómo se pueden definir
condiciones y acciones para diferentes estados del clima, y cómo estas acciones
se aplican al entorno según las condiciones actuales.
"""
class CondicionAccion:
    def __init__(self, condicion, accion):  
        self.condicion = condicion  
        self.accion = accion  

class Ambiente:
    def __init__(self, estado_inicial):  
        self.estado = estado_inicial  

    def aplicar_accion(self, cond_accion):  
        if cond_accion.condicion(self.estado):  
            self.estado = cond_accion.accion(self.estado)  
            return True  
        else:
            return False  

if __name__ == "__main__":
    def clima_soleado(estado):  
        return estado['clima'] == 'soleado'

    def clima_lluvioso(estado):  
        return estado['clima'] == 'lluvioso'

    def accion_salir_exterior(estado):  
        print("¡Sal al exterior!")  
        return estado  

    def accion_quedarse_adentro(estado):  
        print("Quédate en casa.")  
        return estado  

    estado_inicial = {'clima': 'soleado'}  
    ambiente = Ambiente(estado_inicial)  

    cond_accion_soleado = CondicionAccion(clima_soleado, accion_salir_exterior)  
    cond_accion_lluvioso = CondicionAccion(clima_lluvioso, accion_quedarse_adentro)  

    ambiente.aplicar_accion(cond_accion_soleado)  
    ambiente.aplicar_accion(cond_accion_lluvioso)  
