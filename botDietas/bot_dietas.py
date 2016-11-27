import telebot # Importamos las librería
#import pg
import psycopg2
import os

import sqlite3

TOKEN = '280531529:AAHnCDXdiA5yUFQtH6ChpLbvpuUDQi1S4tY'

tb = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API.


def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            print (m.text)


    def conecta():
        try:
            con = sqlite3.connect('bd_dietas.db')
            cursor = con.cursor()
            cursor.execute("SELECT NOMBRE, CANTIDAD, IMPORTANCIA from COMIDA")
            print ("Todo ok.")
            for i in cursor:
                respuesta = i
        except:
            respuesta = 0
        return respuesta

@tb.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    cadena = "Bienvenido al bot. Los comandos a usar son los siguientes:" + "\n" + "/dietas_hoy Devuelve el menú del día de hoy. " + "\n" + "/dietas_general  Muestra el menú de toda la semana." + "\n" + "/informacion ¿Qué es esto?"
    tb.send_message(cid,cadena)



@tb.message_handler(commands=['informacion'])
def informacion(m):
    cid = m.chat.id
    cadena = "Este bot tiene como función ayudarte a recordar cuál es la comida a preparar para el día de hoy y/o la semana actual"
    tb.send_message(cid, cadena)

#
# @tb.message_handler(commands=['incluye_tu_dieta'])
# def informacion(m):
#     cid = m.chat.id
#     cadena = "Incluye tu dieta"
#     tb.send_message(cid, cadena)



@tb.message_handler(commands=['dietas_hoy'])
def dietas_hoy(m):
    cid = m.chat.id
    respuesta = "Las dietas son:" + "\n"
    try:
        con = sqlite3.connect('bd_dietas.db')
        cursor = con.cursor()

        # cursor.execute('''CREATE TABLE COMIDA
        #         (NOMBRE TEXT PRIMARY KEY NOT NULL,
        #         CANTIDAD INT             NOT NULL,
        #         IMPORTANCIA TEXT)''')
        # print ("Se ha creado la tabla.")
        # cursor.execute("INSERT INTO COMIDA (NOMBRE, CANTIDAD, IMPORTANCIA) VALUES ('Risotto', '100', 'Alta')")
        # //print ("Se han introducido los datos.")
        # con.commit() #Para guardar los datos.

        cursor.execute("SELECT NOMBRE, CANTIDAD, IMPORTANCIA from COMIDA")
        for i in cursor:
            respuesta = i

        # cursor.close()
        # conecta.close()
    except:

         respuesta = "Imposible conectarse con la BD."

    tb.send_message(cid, respuesta)

tb.set_update_listener(listener)

tb.polling(none_stop=True)
#
# if __name__ == "__main__":
