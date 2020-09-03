import unittest
from ejercicios1 import mes_a_letras


class Testing(unittest.TestCase):
    def test_mes_a_letras(self):
        resultado = mes_a_letras(2)
        self.assertEqual(resultado, 'Febrero')

    def test_mes_a_letras_otro(self):
        resultado = mes_a_letras(4)
        self.assertEqual(resultado, 'Abril')


if __name__ == '__main__':
    unittest.main()
