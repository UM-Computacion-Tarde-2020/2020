
import unittest
from funciones import funcion 

class Testing(unittest.TestCase):

    def test_lista(self): 
        resultado = funcion(10)
        self.assertEqual(resultado,[1,2,3,4,5,6,7,8,9,10])
unittest.main()        

