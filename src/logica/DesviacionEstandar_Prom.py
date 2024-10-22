import math

class DesviacionEstandar:
    def __init__(self, desviacionE):
        self.__desviacionE = desviacionE

    def promedio(self):
        if len(self.__desviacionE) > 0:
            return sum(self.__desviacionE) / len(self.__desviacionE)
        else:
            return None

    def calcular(self):
        if len(self.__desviacionE) > 1:
            media = sum(self.__desviacionE) / len(self.__desviacionE)
            varianza = sum((x - media) ** 2 for x in self.__desviacionE) / len(self.__desviacionE)
            return math.sqrt(varianza)
        else:
            return None



