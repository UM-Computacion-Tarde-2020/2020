import unittest 
from ejercicios import mes_a_letras
                                                    

class Testing(unittest.TestCase):
    def test_mes_a_letras(self):
        resultado = mes_a_letras(5) 
        self.assertEqual(resultado, 'Mayo') #resultado guarda el valor de nombre_mes definido en la funcion


if __name__ == '__main__': 
    unittest.main()
