#!/bin/usr/python
# -*- coding: utf-8 -*-
import unittest
import based_dietas


# class TestMetodosBot(unittest.TestCase):

#TEST PARA SQLITE

# def nombre():
#     con = sqlite3.connect('bd_dietas.db')
#     cursor = con.cursor()
#     cursor.execute("SELECT nombre, CANTIDAD, IMPORTANCIA from COMIDA")
#     for i in cursor:
#         respuesta = i[0]
#     return respuesta
#
# def extraer_cantidad():
#     con = sqlite3.connect('bd_dietas.db')
#     cursor = con.cursor()
#     cantidad=0
#     cursor.execute("SELECT NOMBRE, CANTIDAD, IMPORTANCIA from COMIDA")
#     for i in cursor:
#         cantidad+=1
#     return cantidad
#
# def test_nombre():
#     """ Test que comprueba si pueden recogerse los datos de la BD. """
#     respuesta = nombre()
#     assert (respuesta =="Risotto")
#
#
# def test_cantidad():
#     """ Test que comprueba la cantidad de datos en la BD. """
#     ndatos = extraer_cantidad()
#     assert (ndatos != 0)


#TEST PARA POSTGRESQL
class TestMetodosBot(unittest.TestCase):

    def test_hay_valores(self):
        """Test para comprobar que hay algún dato en la base de datos."""
        ndatos = based_dietas.ndatos_comida()
        self.assertNotEqual(ndatos,0)

    def test_comida(self):
        """Test para comprobar que hay un elemento concreto."""
        existe_elemento = based_dietas.nombre_comida()
        self.assertTrue(existe_elemento)


if __name__ == '__main__':
    unittest.main()
