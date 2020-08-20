import unittest
from main import suma


class Testing(unittest.TestCase):
    def test_suma_primer_caso(self):
        resultado = suma(2, 2)
        self.assertEqual(resultado, 4)

    def test_suma_segundo_caso(self):
        resultado = suma(4, 4)
        self.assertEqual(resultado, 8)

    def test_suma_tercer_caso(self):
        resultado = suma(4, 5)
        self.assertEqual(resultado, 9)     


if __name__ == '__main__':
    unittest.main()
