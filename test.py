#!/bin/usr/python
# -*- coding: utf-8 -*-

import unittest
import bot_dietas
import pytest

class TestMetodosBot(unittest.TestCase):

    #Comprueba conexión a base de datos.
    def test_menu(self):

        try:
            conecta = psycopg2.connect(database="bd_dietas", user="mmar_bd", password="mmar_bd", host="localhost")
            cursor = conecta.cursor()
            sql = "select * from public.comida"
            cursor.execute(sql)
            r = cursor.fetchall()
            cursor.close()
            conecta.close()
            valor = true
        except:
            valor = false

        self.assertTrue(valor)



if __name__ == '__main__':
    unittest.main()
