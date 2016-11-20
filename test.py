#!/bin/usr/python
# -*- coding: utf-8 -*-

import unittest
import bot_dietas
import pytest

class TestMetodosBot(unittest.TestCase):

    #Comprueba conexión a base de datos.
    def test_menu(self):

            conecta = psycopg2.connect(database="bd_dietas", user="mmar_bd", password="mmar_bd", host="localhost")
            cursor = conecta.cursor()
            sql = "insert into comida values ('Pollo', '1', 'Alta')"
            cursor.execute(sql)
            r = cursor.fetchone()
            respuesta = str(r[0])
            self.assertEqual(respuesta, 'Pollo')




if __name__ == '__main__':
    unittest.main()
