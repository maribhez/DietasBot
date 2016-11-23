#!/bin/usr/python
# -*- coding: utf-8 -*-

import unittest
import bot_dietas
import psycopg2
import pytest

class TestMetodosBot(unittest.TestCase):

    #Comprueba conexión a base de datos.
    def conecta():
        conecta = psycopg2.connect(database="bd_dietas", user="mmar_bd", password="mmar_bd", host="localhost")
        cursor = conecta.cursor()
        sql = "insert into comida values ('Pollo', '100', 'Alta')"
        cursor.execute(sql)
        sql = "select * from public.comida"
        cursor.execute(sql)
        r = cursor.fetchone()
        respuesta = "Menú: " + str(r[0]) + "" + " Cantidad (gramos): " + str(r[1]) + "Importancia" + str(r[2])
        conecta.close()
        cursor.close()
        return respuesta

    def test_menu(self):

        respuesta = conecta()
        self.assertEqual(respuesta, 'Menú: Pollo Cantidad (gramos):100ImportanciaAlta')




    if __name__ == '__main__':
        unittest.main()
