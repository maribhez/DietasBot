import telebot # Importamos las librería
#import pg
import psycopg2
import os

TOKEN = '280531529:AAHnCDXdiA5yUFQtH6ChpLbvpuUDQi1S4tY'

tb = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API.
# usuario = 'postgres'
# base_datos = 'bd_dietas'
# passw = 'postgres'


def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            print (m.text)

def conecta_bd():
    valor = true
    try:
        conecta = psycopg2.connect(database="bd_dietas", user="mmar_bd", password="mmar_bd", host="localhost")
        cursor = conecta.cursor()
        sql = "select * from public.comida"
        cursor.execute(sql)
        r = cursor.fetchall()
        cursor.close()
        conecta.close()
    except:
        valor = false
    return valor

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



@tb.message_handler(commands=['dietas_hoy'])
def dietas_hoy(m):
    cid = m.chat.id
    try:
        conecta = psycopg2.connect(database="bd_dietas", user="mmar_bd", password="mmar_bd", host="localhost")
        cursor = conecta.cursor()
        #respuesta = cursor.fetchall()

    except:
        tb.send_message(cid, "No conecta -2 ")
    try:
        #sql = "insert into comida values ('Pollo', '1', 'Alta')"
        #cursor.execute(sql)
        sql = "select * from public.comida"
        cursor.execute(sql)
        #respuesta = "Correcto."
        r = cursor.fetchall()
        # respuesta = ""
        # for i in r:
        #     respuesta += str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n"
        respuesta = "Conectado a la BD"
        cursor.close()
        conecta.close()
    except:

         respuesta = "Imposible conectarse con la BD."

    tb.send_message(cid, respuesta)

tb.set_update_listener(listener)

tb.polling(none_stop=True) #Así no para nunca el bot.


if __name__ == "__main__":
    dietas_hoy();
