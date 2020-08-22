import unittest
from main import suma


class Testing(unittest.TestCase):
    def test_suma_primer_caso(self):
        resultado = suma(2, 2)
        self.assertEqual(resultado, 4)


if __name__ == '__main__':
    unittest.main()
