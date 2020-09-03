import unittest
from ejercicios import mes_a_letras
​
​
class Testing(unittest.TestCase):
    def test_mes_a_letras(self):
        resultado = mes_a_letras(2)
        self.assertEqual(resultado, 'Febrero')
​
​
if __name__ == '__main__':
    unittest.main()
