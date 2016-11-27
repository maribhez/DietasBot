#!/bin/usr/python
# -*- coding: utf-8 -*-
import sqlite3
# class TestMetodosBot(unittest.TestCase):

def nombre():
    con = sqlite3.connect('bd_dietas.db')
    cursor = con.cursor()
    cursor.execute("SELECT NOMBRE, CANTIDAD, IMPORTANCIA from COMIDA")
    for i in cursor:
        respuesta = i[0]
    return respuesta

def extraer_cantidad():
    con = sqlite3.connect('bd_dietas.db')
    cursor = con.cursor()
    cantidad=0
    cursor.execute("SELECT NOMBRE, CANTIDAD, IMPORTANCIA from COMIDA")
    for i in cursor:
        cantidad+=1
    return cantidad

def test_nombre():
    """ Test que comprueba si pueden recogerse los datos de la BD. """
    respuesta = nombre()
    assert (respuesta =="Risotto")


def test_cantidad():
    """ Test que comprueba la cantidad de datos en la BD. """
    ndatos = extraer_cantidad()
    assert (ndatos != 0)


#
# if __name__ == '__main__':
#     unittest.main()
