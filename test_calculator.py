
import unittest
from calculator import calcular


class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(calcular(2, "+", 3), 5)

    def test_subtracao(self):
        self.assertEqual(calcular(8, "-", 3), 5)

    def test_multiplicacao(self):
        self.assertEqual(calcular(4, "*", 3), 12)

    def test_divisao(self):
        self.assertEqual(calcular(10, "/", 2), 5)

    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calcular(10, "/", 0)

    def test_operador_invalido(self):
        with self.assertRaises(ValueError):
            calcular(2, "%", 3)


if __name__ == "__main__":
    unittest.main()
