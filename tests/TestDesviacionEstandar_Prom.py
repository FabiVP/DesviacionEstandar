import unittest
from src.logica.DesviacionEstandar_Prom import DesviacionEstandar_Prom

class TestDesviacionEstandar_Prom(unittest.TestCase):
    def test_sin_elementos(self):
        elementos = DesviacionEstandar_Prom([])
        self.assertIsNone(elementos.promedio())

    def test_unElemento_retornaValorUnicoElemento(self):
        elementos = DesviacionEstandar_Prom([15])
        self.assertEqual(15, elementos.promedio())

    def test_dosElementos_retornaPromedioElementos(self):
        elementos = DesviacionEstandar_Prom([15, 17])
        self.assertEqual(16, elementos.promedio())

    def test_nElementos_retornaPromedioNElementos(self):
        elementos = DesviacionEstandar_Prom([12, 14, 18, 19, 10, 15])
        self.assertEqual((12 + 14 + 18 + 19 + 10 + 15) / 6, elementos.promedio())