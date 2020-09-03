import unittest
from funcion import funcion_que_hace_algo


class Testing(unittest.TestCase):
    def test_string(self):
        result = funcion_que_hace_algo()
        self.assertEqual(result, "hola mundo")


if  __name__ == '__main__':
    unittest.main()