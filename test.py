#!/bin/usr/python
# -*- coding: utf-8 -*-

import unittest
import bot_dietas


class TestMetodosBot(unittest.TestCase):

    #Comprueba conexión a base de datos.
    def test_menu(self):
        valor = bot_dietas.conecta_bd()
        self.assertTrue(valor)


if __name__ == '__main__':
    unittest.main()
