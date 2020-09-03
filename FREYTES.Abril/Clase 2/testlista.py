import unittest
from lista import funcion


class testing(unittest.TestCase):
    def test_lista(self):
        extremo = 3
        resultado = funcion(extremo)
        lista_esperada = [i for i in range(1, extremo + 1)]
        self.assertEqual(resultado, lista_esperada)


if __name__ == '__main__':
    unittest.main()
