import unittest
from listas import funcion


class Testing(unittest.TestCase):
    def test_lista(self):
        extremo = 5000
        resultado = funcion(extremo)
        lista_esperada = [i for i in range(1, extremo + 1)]
        self.assertEqual(resultado, lista_esperada)
        

if __name__ == '__main__':
    unittest.main()
