import unittest
from main import split


class Testing(unittest.TestCase):
    def test_extraer_impares(self):
        list = [i for i in range(0, 100)]
        list_test = split(list)
        list_impar = [i for i in range(1, 100, 2)]
        self.assertEqual(list_test, list_impar)


if __name__ == '__main__':
    unittest.main()
