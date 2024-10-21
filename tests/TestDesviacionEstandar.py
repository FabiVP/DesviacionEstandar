import unittest
from src.logica.DesviacionEstandar import DesviacionEstandar

class TestDesviacionEstandar(unittest.TestCase):
    def test_desviacionEstandar_nElementos(self):
        desviacionE = DesviacionEstandar([10, 12, 23, 23, 16, 23, 21, 16])
        # Calculamos el valor esperado manualmente
        media = (10 + 12 + 23 + 23 + 16 + 23 + 21 + 16) / 8
        varianza = ((10 - media) ** 2 + (12 - media) ** 2 + (23 - media) ** 2 +
                    (23 - media) ** 2 + (16 - media) ** 2 + (23 - media) ** 2 +
                    (21 - media) ** 2 + (16 - media) ** 2) / 8
        esperado = varianza ** 0.5

        self.assertAlmostEqual(desviacionE.calcular(), esperado, places=5)


