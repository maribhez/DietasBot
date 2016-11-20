#!/bin/usr/python
# -*- coding: utf-8 -*-

import unittest
import bot_dietas
import pytest

class TestMetodosBot(unittest.TestCase):

    #Comprueba conexión a base de datos.
    def test_menu(self):
        valor = bot_dietas.conecta_bd()
        self.assertTrue(valor)


def main():
        unittest.main()


if __name__ == '__main__':
    unittest.main()
