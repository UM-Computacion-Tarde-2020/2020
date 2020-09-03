import unittest
from listas import funcion


class Testing(unittest.TestCase):                           #en comentarios otra forma de hacer
    def test_lista(self):
        extremo = 5000                                      #este se debe sacar
        resultado = funcion(extremo)                        #funcion (500)
        lista_esperada =[i for i in range(1,extremo + 1)]   #range(1,501)
        self.assertEqual(resultado, lista_esperada)      
 
     
if __name__ == '__main__':
    unittest.main()
