#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import psycopg2, psycopg2.extras



def conectaBD():
    cadena = "host= 'localhost' dbname='BD_BOTDIETAS' user='mmar_bd' password = 'mmar_bd'"
    conn =  psycopg2.connect(cadena)
    cur = conn.cursor()
    return cur

def conecta():

    ##Datos para la conexión. Funciona OK.
    cadena = "host= 'localhost' dbname='BD_BOTDIETAS' user='mmar_bd' password = 'mmar_bd'"
    try:
        conn =  psycopg2.connect(cadena)
    except:
        print ("Imposible Conexión. ")
    try:
        cur = conn.cursor()
        respuesta = 0
        # comando = """CREATE TABLE COMIDA (id_comida INT PRIMARY KEY NOT NULL,
        #                                      nombre TEXT NOT NULL,
        #                                      cantidad TEXT NULL)"""
        comando = """CREATE TABLE COMIDAS_MENU (id_menu_fusion INT NOT NULL,
                                        id_comida_fusion INT NOT NULL,
                                        hora VARCHAR(50) NOT NULL,
                                        día_semana VARCHAR(10) NOT NULL)"""

        cur.execute(comando)
        print ("Se ha creado la tabla.")
        conn.commit()
        # comando = """ INSERT INTO COMIDA (id_comida, nombre, cantidad) VALUES (1, 'Pollo asado', 100)"""
        # cur.execute(comando)
        # # print ("Se han introducido los datos.")
        # conn.commit()  #Para guardar los datos.
        # comando = """SELECT * from COMIDA"""
        # cur.execute(comando)
        # rows = cur.fetchall()
        # # print (rows)
        # for i in rows:
        #     respuesta += str(i[0] + " " + str(i[1]) + " " + str(i[2]) + "\n")
        # return respuesta

    #
    #     # result = conecta.query(consulta)
    #     # conecta.close()
    #     # return result
    #     # #
    #     # for i in resultado:
    #     #     respuesta += str(i[1] + " " + str(i[2]) + " " + str(i[3]) + "\n")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def ndatos_comida():
    cur = conectaBD()
    comando = """SELECT * from COMIDA"""
    cur.execute(comando)
    ndatos = len(cur.fetchall())
    return ndatos


def nombre_comida():
    cur = conectaBD()
    comando = """SELECT * from COMIDA where nombre = 'Pollo asado' """
    cur.execute(comando)
    n = len(cur.fetchall())
    if n!= 0:
        return True
    return false
