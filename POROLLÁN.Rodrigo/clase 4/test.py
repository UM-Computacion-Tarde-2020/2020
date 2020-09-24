import unittest 
from main import split

class Testing(unittest.TestCase):
    def test_extraer_impares(self):
        list = [i for i in range(0, 100)]
        list_test = split(list)
        list_impar = [i for i in range(1, 100, 2)]
        self.assertEqual(list_test, list_impar) 
        
    def test_otros_impares(self):
        list = [1, 4, 5, 8, 11, 16]
        list_test = split(list)
        self.assertEqual(list_test, [1, 5, 11])
        
        
if __name__ == '__main__':
    unittest.main()


