
import unittest
from network import porta_valida


class TestValidacaoPorta(unittest.TestCase):

    def test_porta_minima(self):
        self.assertTrue(porta_valida(1))

    def test_porta_maxima(self):
        self.assertTrue(porta_valida(65535))

    def test_porta_zero(self):
        self.assertFalse(porta_valida(0))

    def test_porta_acima_limite(self):
        self.assertFalse(porta_valida(65536))

    def test_porta_negativa(self):
        self.assertFalse(porta_valida(-1))

    def test_texto_invalido(self):
        self.assertFalse(porta_valida("443"))

    def test_numero_decimal(self):
        self.assertFalse(porta_valida(443.5))


if __name__ == "__main__":
    unittest.main()
