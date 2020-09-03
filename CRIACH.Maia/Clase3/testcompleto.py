import unittest
from ejercicios import mes_a_letras_reves
from parameterized import parameterized


class Testing(unittest.TestCase):
    @parameterized.expand([[1, 'Enero'], [2, 'Febrero'],
                           [3, 'Marzo'], [4, 'Abril'],
                           [5, 'Mayo'], [6, 'Junio'],
                           [7, 'Julio'], [8, 'Agosto'],
                           [9, 'Septiembre'], [10, 'Octubre'],
                           [11, 'Noviembre'], [12, 'Diciembre']])
    def test_mes_a_letras_reves(self, mes, name):
        resultado = mes_a_letras_reves(mes)
        self.assertEqual(resultado, name)


if __name__ == '__main__':
    unittest.main()
