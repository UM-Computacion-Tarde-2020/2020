import unittest
from funcion import funcion


class Testing(unittest.TestCase):
    def test_lista(self):
        extremo = 500
        resultado = funcion(extremo)
        lista_esperada
        self.assertEqual(resultado, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == '__main__':
    unittest.main()
