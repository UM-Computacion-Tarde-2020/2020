import unittest
from ejercicios import mes_a_letras
from parameterized import parameterized


class Testing(unittest.TestCase):
    @parameterized.expand([[1, 'Enero'], [2, 'Febrero'],
                           [3, 'Marzo'], [4, 'Abril'],
                           [5, 'Mayo'], [6, 'Junio'],
                           [7, 'Julio'], [8, 'Agosto'],
                           [9, 'Septiembre'], [10, 'Octubre'],
                           [11, 'Noviembre'], [12, 'Diciembre']])
    def test_mes_a_letras(self, mes, name):
        resultado = mes_a_letras(mes)
        self.assertEqual(resultado, name)


# utilizo este tipo de código cuando quiero probar una función de muchos parametros
# en vez de escribir muchas funciones utilizo arroba que se denomina decorador


if __name__ == '__main__':
    unittest.main()
