import unittest
from funciones import funcion_1
from funciones import funcion_2


class Testing(unittest.TestCase):
    def test_string(self):
        result = funcion_1()
        self.assertEqual(result, "Hola Mundo")

    def test_otro(self):
        result = funcion_2()
        self.assertEqual(result, 154.5)


if __name__ == '__main__':
    unittest.main()
