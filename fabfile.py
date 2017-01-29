from fabric.api import sudo, cd, env, run, shell_env
import os

#Paso inicial para poner a punto nuestra máquina.
def instala():

    #Descargamos nuestra aplicación desde GitHub.
    run('git clone https://github.com/maribhez/DietasBot.git')

    #Entramos a la carpeta recién creada e instalamos los requisitos.
    run('cd DietasBot && pip install -r requirements.txt')

#Función para lanzar nuestra aplicación.
def ejecutar():
    with shell_env(HOST_BD=os.environ['HOST_BD'],
                    USER_BD=os.environ['USER_BD'],
                    PW_BD=os.environ['PW_BD'],
                    NAME_BD=os.environ['NAME_BD'],
                    TOKENBOT=os.environ['TOKENBOT']
                   ):
