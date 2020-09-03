import unittest
from funciones import funcion_que_hace_algo
from funciones import funcion_que_hace_otra_cosa


class Testing(unittest.TestCase):
    def test_string(self):
        result = funcion_que_hace_algo()
        self.assertEqual(result, "Hola Mundo")

    def test_string2(self):
        result = funcion_que_hace_otra_cosa()
        self.assertEqual(result, 154.5)


if __name__ == '__main__':
    unittest.main()
