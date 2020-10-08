import unittest
from ejercicios import mes_a_letras


class Testing(unittest.TestCase):
    def test_mes_a_letras(self):
        resultado = mes_a_letras(2)
        self.assertEqual(resultado, "Febrero")

    def test_mes_a_letras_dos(self):
        resultado = mes_a_letras(6)
        self.assertEqual(resultado, "Junio")

#todo lo escrito en payton con un arroba es un decorador, permite mandar parámetros a la funcion para probarla
if __name__ == "__main__":
    unittest.main()
