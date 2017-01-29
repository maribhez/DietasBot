from fabric.api import *
import os

#Paso inicial para poner a punto nuestra maquina.
def instala():

    #Aseguramos la limpieza de la maquina.
    run ('sudo rm -rf DietasBot')

    #Descargamos nuestra aplicacion desde GitHub.
    run('git clone https://github.com/maribhez/DietasBot.git')

    #Entramos a la carpeta recien creada e instalamos los requisitos.
    run('cd DietasBot && pip install -r requirements.txt')

#Funcion para lanzar nuestra aplicacion.
def ejecutar():

    with shell_env(HOST_BD=os.environ['HOST_BD'],
                    USER_BD=os.environ['USER_BD'],
                    PASS_BD=os.environ['PASS_BD'],
                    NAME_BD=os.environ['NAME_BD'],
                    TOKENBOT=os.environ['TOKENBOT']
                   ):
        run('sudo supervisorctl start botdietas')

def detener():
    run ('sudo supervisorctl stop botdietas')

def borrado():
    run ('sudo rm -rf DietasBot')

def test():
    with shell_env(HOST_BD=os.environ['HOST_BD'],
                    USER_BD=os.environ['USER_BD'],
                    PASS_BD=os.environ['PASS_BD'],
                    NAME_BD=os.environ['NAME_BD'],
                    TOKENBOT=os.environ['TOKENBOT']
                   ):
        run('cd DietasBot/botDietas && python test_bot.py')
