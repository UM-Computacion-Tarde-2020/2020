import unittest
from funciones import funcion_que_hace_algo
from funciones import funcion_que_hace_otra_cosa


class testing(unittest.TestCase):
    pass
    def test_string(self):
        result = funcion_que_hace_algo()
        self.assertEqual(result, "Hola mundo")

    def test_algo(self):
        result = funcion_que_hace_otra_cosa()
        self.assertEqual(result, 145.5)

if __name__ == '__main__':
    unittest.main()        
        
        



