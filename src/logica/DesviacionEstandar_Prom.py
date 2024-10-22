import math

class DesviacionEstandar_Prom:
    def __init__(self, numeros):
        self.__numeros = numeros

    def promedio(self):
        if len(self.__numeros) == 0:
            return "No Se Puede Calcular"
        if len(self.__numeros) > 0:
            return sum(self.__numeros) / len(self.__numeros)
        else:
            return None

    def calcular(self):
        if len(self.__numeros) == 0:
            return "No Se Puede Calcular"
        elif len(self.__numeros) == 1:
            return 0
        else:
            media = sum(self.__numeros) / len(self.__numeros)
            varianza = sum((x - media) ** 2 for x in self.__numeros) / len(self.__numeros)
            return math.sqrt(varianza)



