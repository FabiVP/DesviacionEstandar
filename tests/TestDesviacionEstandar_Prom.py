import math
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

    def test_nElementosTodosCeros(self):
        elementos = DesviacionEstandar_Prom([0, 0, 0, 0])
        self.assertEqual(0, elementos.promedio())

    def test_nElementosPositivosYNegativos(self):
        elementos = DesviacionEstandar_Prom([10, -10, 20, -20])
        self.assertEqual((10 + (-10) + 20 + (-20)) / 4, elementos.promedio())

    def test_elementosNoNumericos_lanzaTypeError(self):
        with self.assertRaises(TypeError):
            elementos = DesviacionEstandar_Prom([10, "no_numero", 20])
            elementos.promedio()

# Desvicion estandar
    def test_sin_elementos_desviacion(self):
        elementos = DesviacionEstandar_Prom([])
        self.assertIsNone(elementos.calcular())

    def test_unElemento_desviacionCero(self):
        elementos = DesviacionEstandar_Prom([15])
        self.assertEqual(0, elementos.calcular())

    def test_dosElementos_desviacion(self):
        elementos = DesviacionEstandar_Prom([15, 17])
        # cálculo manual: sqrt(((15-16)^2 + (17-16)^2) / 2) = sqrt(1) = 1
        self.assertEqual(1, elementos.calcular())

    def test_nElementosPositivos_desviacion(self):
        elementos = DesviacionEstandar_Prom([12, 14, 18, 19, 10, 15])
        # cálculo manual
        media = (12 + 14 + 18 + 19 + 10 + 15) / 6
        varianza = sum((x - media) ** 2 for x in [12, 14, 18, 19, 10, 15]) / 6
        desviacion = math.sqrt(varianza)
        self.assertAlmostEqual(desviacion, elementos.calcular())