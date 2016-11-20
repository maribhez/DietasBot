#!/usr/bin/python

import pg
import os, sys




def dieta_hoy():

    try:
        conecta = pg.connect(dbname=base_datos, user=usuario, password=passw)
        consulta = 'select * from Comida'
        result = conecta.query(consulta)
        conecta.close()
        return result
        #
        # for i in resultado:
        #     respuesta += str(i[1] + " " + str(i[2]) + " " + str(i[3]) + "\n")


    except:
        print ("Imposible conectar con la BD.")
