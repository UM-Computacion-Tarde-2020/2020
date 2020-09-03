import unittest
from ejercicios import mes_a_letras
from ejercicios import mes_a_letras_reves


class Testing(unittest.TestCase):
    def test_mes_a_letras(self):
        resultado = mes_a_letras(3)
        self.assertEqual(resultado, "Marzo")

    def test_mes_a_letras_reves(self):
        resultado = mes_a_letras_reves(3)
        self.assertEqual(resultado, "Marzo")


if __name__ == '__main__':
    unittest.main()
