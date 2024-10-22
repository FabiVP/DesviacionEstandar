import unittest
from src.logica.DesviacionEstandar_Prom import DesviacionEstandar_Prom

class TestDesviacionEstandar_Prom(unittest.TestCase):
    def test_sin_elementos(self):
        elementos = DesviacionEstandar_Prom([])
        self.assertIsNone(elementos.promedio())



