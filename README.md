# BOT DE TELEGRAM PARA EL APOYO DE DIETAS ALIMENTICIAS.

<!-- ![Sin titulo](https://travis-ci.org/maribhez/Infraestructura-Virtual-2016-2017.svg?branch=master) -->

<!-- [![Build Status](https://travis-ci.org/maribhez/DietasBot.svg?branch=master)](https://travis-ci.org/maribhez/DietasBot) -->
[logo]: http://i345.photobucket.com/albums/p391/maribhez/photo_2016-12-11_21-13-22_zpscejb1fjf.jpg
[enlace-heroku]:https://botdietas.herokuapp.com/

[![Logo heroku][logo]][enlace-heroku]

*****

## Descripción  y justificación.

Se va a llevar a cabo la realización de un *bot de telegram* donde se almacenen dietas alimenticias (y quizá más información que vaya surgiendo durante la realización del mismo) tanto añadidas por el usuario de dicha aplicación (mediante una aplicación que se creará más adelante) como definidas por defecto a la hora de crear el bot.

Lo que permitirá ésto será tanto consultar dietas completas como poder recordar qué plato es el que tienes que elegir para seguir tu dieta sin más que coger el teléfono, por ejemplo. Se estudiará la posibilidad de añadir recetas y así poder mejorar nuestras dotes en la cocina.

****

## Servicios y herramientas.

1. Uso de *PostgreSQL* como base de datos.
2. Uso de *Travis-ci* para conseguir la integración continua y comprobar que el entorno funciona de forma correcta.
3. Este bot está desarrollado sobre *Python 3.5.2*.
4. Para el uso y prueba de este bot se usa la API de Telegram.
5. Será necesario un servicio en la nube para poder desplegar nuestro bot.

****

##Integración continua.

Tal y como una de las herramientas indica se ha configurado integración continua para este proyecto, y en este caso se ha *Travis-ci*.

Dicha configuración se encuentra enlazada a la cuenta de GitHub, además de crear un archivo *.travis.yml* que indica todo lo necesario para la puesta a punto de la prueba del proyecto.

Para que Travis configure nuestro proyecto para poder realizar las pruebas se ha creado un *makefile*. Dicho archivo contiene la siguiente información:

>  install:
>  	pip install -r requirements.txt
>
>
>  test:
>  		cd botDietas && pytest
>
>  ejecutar:
>  	cd botDietas && python bot_dietas.py



##Despliegue en un PASS.

Para este hito he creado una cuenta en *Heroku*, y ese ha sido el primer paso para configurar el despliegue.

Después, he creado una aplicación con su correspondiente base de datos (*de PostgreSQL*) con los comandos **heroku create** y **heroku addons:create heroku-postgresql:hobby-dev --app botdietas**, siendo *botdietas* el nombre de la aplicación anteriormente creada. Para poder crear esto sin fallos es necesario hacer login en nuestra cuenta con el comando **heroku login**.

Una vez creada la aplicación y la BD es necesario sincronizarlo con GitHub y el repositorio donde estamos desarrollando la aplicación para poder usar esta configuración más tarde.

Y además, tal y como aparece en la siguiente captura tenemos que hacer que el despliegue de la aplicación se realice de forma automática pero habiendo pasado antes por *Travis-CI*.

![Configuracion](http://i345.photobucket.com/albums/p391/maribhez/configuracionGitHub_zpsjxsrl2jq.png "Configuracion")


Lo siguiente es establecer las *variables de entorno* tanto en Travis-CI como en Heroku. Tenemos que establecer como variables de entorno las credenciales de la base de datos creada en Heroku y el Token del bot de Telegram.


Además, para que Heroku sepa qué tiene que ejecutar tenemos que crear un fichero denominado *Procfile* con el siguiente contenido:

> worker: python botDietas/bot_dietas.py


Y, por último, para dar a conocer la versión de Python sobre la que estamos trabajando creamos un fichero *runtime.txt* donde sólo será necesario añadir lo siguiente:

> python-3.5.2


Y ya, para finalizar, se pone en funcionamiento nuestra aplicación con el comando:

> heroku ps:scale worker=1 --app botdietas


Podemos ver que la aplicación está funcionando de forma adecuada accediendo a los *logs* proporcionados por Heroku desde terminal o desde la página web.


Si accedemos desde la página web se nos presenta algo como esto:

![Logs](http://i345.photobucket.com/albums/p391/maribhez/log_zps3swjszot.png "Logs en funcionamiento")


Tras esto, ya sólo quedaría acceder a Telegram al bot "@DietasBot" para probar su funcionamiento.

## Entorno de pruebas.

[Repositorio Docker](https://hub.docker.com/r/mmaribanhez/botdietas/)

Esta configuración y este hito lo he realizado sobre Ubuntu, por lo que la instalación ya estaba realizada por los ejercicios correspondientes a la misma asignatura.

Las primeras pruebas llevadas a cabo fueron las pruebas en local, y sus pasos fueron los siguientes.

* Creación de archivo Dockerfile.

Principalmente, la información pasada al archivo ha sido el sistema operativo a usar, las variables de entorno y argumentos que se le pasaran a la ejecución del contenedor y aquello que es necesario instalar.
~~~
FROM ubuntu:14.04

MAINTAINER Maria del Mar Ibañez Hernandez  <mmaribanhez@correo.ugr.es>

# Variables de entorno para poder conectarse a la base de datos
ARG DATABASE_URL
ARG HOST_BD
ARG NAME_BD
ARG PW_BD
ARG TOKENBOT
ARG USER_BD

ENV DATABASE_URL=$DATABASE_URL
ENV HOST_BD=$HOST_BD
ENV NAME_BD=$NAME_BD
ENV PW_BD=$PW_BD
ENV TOKENBOT=$TOKENBOT
ENV USER_BD=$USER_BD

RUN apt-get update


# Instalamos python
RUN apt-get install -y python-setuptools
RUN apt-get install -y python-dev
RUN apt-get install -y build-essential
RUN apt-get install -y python-psycopg2
RUN apt-get install -y libpq-dev
RUN apt-get install -y python-pip
RUN pip install --upgrade pip

# Instalamos git y descargamos el repositorio
RUN apt-get install -y git
RUN git clone https://github.com/maribhez/DietasBot.git


# Instalamos todo lo necesario para ejecutar el bot
RUN cd DietasBot/ && make install
~~~

* Una vez creado procedemos a la instalación del contenedor con el comando **sudo docker build -t dietasbot ./**, donde dietasbot es el nombre del contenedor. Hemos de tener en cuenta que este comando lo tenemos que usar en la carpeta donde se encuentre el archivo *Dockerfile* del que anteriormente hemos hablado.
![Contenedor inicial](http://i345.photobucket.com/albums/p391/maribhez/Captura_zpsihtzlpqr.png "Contenedor inicial")

 * Ahora tenemos que comprobar que podemos acceder a dicho contenedor con la siguiente linea:

> docker run -e "DATABASE_URL=XXX" -e "HOST_BD=XXXX" -e "NAME_BD=XXXX" -e "PW_BD=XXXX" -e "TOKENBOT=XXXX" -e "USER_BD=XXXX" -i -t dietasbot /bin/bash

Los parámetros a usar son aquellas credenciales correspodientes a la base de datos de Heroku que habíamos usado en anteriores configuraciones y la del bot que estamos desarrollando. Si todo ha funcionado de la forma esperada podremos pasar a la configuración de Docker sobre Docker Hub.


* El siguiente paso es sincronizar nuestra cuenta de *Git Hub* con la cuenta ya creada de *Docker Hub* y crear un repositorio.

![Repositorio](http://i345.photobucket.com/albums/p391/maribhez/Captura2_zps8iaqjx8n.png "Repositorio")

* Tras esto, uan vez que hemos hecho *push* del archivo *Dockerfile* a nuestro repositorio de Git Hub y éste se encuentra actualizado  el repositorio de *Docker Hub* empieza su "Construcción" y se comprueba su correcta funcionamiento.

![Construcción](http://i345.photobucket.com/albums/p391/maribhez/Captura3_zpsacdyhdv3.png "Construccion")

* Y ya, para descargar, no hay más que usar **docker pull mmaribanhez/botdietas**, siendo esta información que podemos sacar del propio repositorio.
 ![Descarga](http://i345.photobucket.com/albums/p391/maribhez/Captura4_zps4x77hhre.png "Descarga")

Vemos aquí cómo aparece nuestra descarga en los repositorios de nuestro sistema.

![Comprobación](http://i345.photobucket.com/albums/p391/maribhez/Captura5_zpsmxial3za.png "Comprobacion")



##Diseño del soporte virtual para el despliegue de una aplicación.


Hemos configurado en este caso todo lo necesario para el despliegue automático a las plataformas de producción.

De entre todas las posibilidades he usado *Vagrant*, *Azure*, *Ansible*, *Fabric* y *Supervisor*. Por supuesto, antes de empezar a explicar todo lo que he realizado explico brevemente qué es cada una de estas herramientas.

* **Vagrant**: Herramienta diseñada para la creación y configuración de entornos de desarrollo virtualizados. Para poder usarlo hemos de tener instalado **VirtualBox**, pudiendo instalarlo usando el siguiente [enlace](https://www.virtualbox.org/ "enlace") .

* **Azure**: Herramienta que proporciona un entorno gestionado para la ejecución y el despliegue de aplicaciones y servicios en la nube.

* **Ansible**:Herramienta que permite gestionar configuraciones, aprovisionamiento de recursos, despliegue automático de aplicaciones y muchas otras tareas de TI de una forma limpia y sencilla.

* **Fabric**: Librería de Python que permite ordenar tareas tanto en la máquina local como en una máquina remota, de forma que podemos ejecutar el despliegue sin usar ssh.

* **Supervisor**: Gestor de procesos para Linux.


### Pasos para el despliegue.

Como ya se ha especificado hemos de tener instalado **VirtualBox** y en caso de ser necesario podemos usar lo siguiente:

~~~
sudo apt update
sudo apt install virtualbox
~~~


Ahora, instalamos tanto Vagrant como el plugin de azure para Vagrant y el CLI de Azure.

~~~
sudo apt install Vagrant
vagrant plugin install vagrant-azure --plugin-version '2.0.0.pre1'
sudo npm install -g azure-cli
~~~

Como siguiente paso nos encontramos con la configuración del archivo **Vagrantfile**, que es el archivo que va a definir nuestra máquina virtual a desplegar.

Nos queda de la siguiente manera, pudiendo verlo en el siguiente [enlace](https://github.com/maribhez/DietasBot/blob/master/Vagrantfile "enlace") y a continuación:

~~~
Vagrant.configure("2") do |config|

  config.vm.box = "azure"
  config.env.enable #enable the plugin
  config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box'
  config.vm.hostname = "localhost"
  config.vm.network "public_network"
  config.vm.network "private_network", ip: "40.68.191.37", virtualbox__intnet: "vboxnet0"
  config.vm.network "forwarded_port", guest: 80, host: 80

  config.ssh.private_key_path = '~/.ssh/id_rsa'


  config.vm.provider :azure do |azure|
    # mgmt_certificate = File.expand_path('C:\Users\Mmar\botdietas\azurevagrant.cer')
    # mgmt_endpoint = 'https://management.core.windows.net'

    azure.vm_image_urn = 'canonical:UbuntuServer:16.04-LTS:16.04.201701130'
    azure.vm_size = 'Basic_A0'
    azure.location = 'westeurope'
    azure.vm_name = 'BOT-DIETAS'
    azure.tcp_endpoints = '80:80'
    azure.vm_password = 'aabbcc'

    azure.tenant_id = ENV['TENANT_ID']
    azure.client_id = ENV['CLIENT_ID']
    azure.client_secret = ENV['CLIENT_SECRET']
    azure.subscription_id =ENV['SUBSCRIPTION_ID']
   end


   #Provisionamiento
   config.vm.provision "ansible" do |ansible|
       ansible.sudo = true
       ansible.playbook = "configuracion.yml"
       ansible.verbose = "-vvvv"
       ansible.host_key_checking = false
  end

end
~~~

Hemos de saber también que las variables de entorno declaradas han sido especificadas en un fichero auxiliar llamado **.env** y que por cuestiones de seguridad no ha sido subido a este repositorio.

Algunas de las variables especificadas han sido, por ejemplo, el nombre de nuestra máquina, imagen de sistema operativo o la configuración de red.

Usando *vagrant up* podemos lanzar nuestra máquina, haciendo notar además que gracias al uso de *Ansible* podemos instalar los paquetes. En la última parte podemos ver que se hace referencia a un archivo llamado **configuracion.yml** y que con el contenido de éste último instalamos todos los paquetes necesarios para el uso de nuestra aplicación.

El contenido es el [siguiente](https://github.com/maribhez/DietasBot/blob/master/configuracion.yml "siguiente").



~~~
- hosts: all
  sudo: yes
  remote_user: vagrant
  vars:
    TOKENBOT: "{{ lookup('env','TOKENBOT') }}"
    USER_BD: "{{ lookup('env','USER_BD') }}"
    PASS_BD: "{{ lookup('env', 'PASS_BD') }}"
    HOST_BD: "{{ lookup('env', 'HOST_BD') }}"
    NAME_BD: "{{ lookup('env', 'NAME_BD') }}"
  tasks:
  - name: Actualizando el sistema.
    command: sudo apt-get update
  - name: Instalar setuptools (de python).
    apt: name=python-setuptools state=present
  - name: Instalar python-dev.
    apt: name=python-dev state=present
  - name: Instalar libpq-dev (python)
    apt: name=libpq-dev state=present
  - name: Instalar build-essential (python)
    apt: name=build-essential state=present
  - name: Instalar python-psycopg2 (python)
    apt: name=python-psycopg2 state=present
  - name: Instalar git
    apt: name=git state=present
  - name: Instalar pip
    apt: name=python-pip state=present
  - name: Instalar API.
    command: sudo pip install python-telegram-bot
  - name: Instalar supervisor
    apt: name=supervisor state=present
  - name: Configuracion supervisor
    template: src=supervisor.conf dest=/etc/supervisor/conf.d/supervisor.conf
  - name: Ejecutar supervisor
    service: name=supervisor state=started
  - name: Instalar BD postgresql
    apt: name=postgresql state=present
    apt: name=postgresql-contrib state=present
  ~~~


La orden **vagrant up --provider=azure** se encarga tanto del despliegue de la máquina como del aprovisionamiento de la misma. Sin embargo, existe un comando específico que nos valdría para la acción de instalación de paquetes: **vagrant provision**.

Vemos también que en el directorio de este repositorio existe otro archivo llamado *ansible.cfg*, y éste se debe a la solución de un error surgido con estas últimas configuraciones.

Después de desplegar y aprovisionar la máquina debemos comunicar con ella y ser capaces de realizar tareas de forma remota.

Por supuesto requiere de una [instalación](http://www.fabfile.org/installing.html "instalación") previa. Tal y como se puede ver en el tutorial el comando a ejecutar es el siguiente:

~~~
pip install fabric
~~~

Aunque también podemos usar:

~~~
sudo apt-get install fabric
~~~

En la configuración de esta herramienta intervienen dos de nuestros archivos: la [configuracion interna](https://github.com/maribhez/DietasBot/blob/master/supervisor.conf "configuracion interna") y el [archivo](https://github.com/maribhez/DietasBot/blob/master/fabfile.py "archivo") donde vamos a definir todas las funciones con las que nos comunicaremos con la máquina y ejecutaremos nuestra aplicación.

El contenido de ambos es el siguiente:

* **Archivo supervisor.conf**:
~~~
# coding: utf-8
from fabric.api import *
import os

#Paso inicial para poner a punto nuestra maquina.
def Instala():

    #Aseguramos la limpieza de la maquina.
    run ('sudo rm -rf DietasBot')

    #Descargamos nuestra aplicacion desde GitHub.
    run('git clone https://github.com/maribhez/DietasBot.git')

    #Entramos a la carpeta recien creada e instalamos los requisitos.
    run('cd DietasBot && pip install -r requirements.txt')

#Funcion para lanzar nuestra aplicacion.
def Ejecutar():

    with shell_env(HOST_BD=os.environ['HOST_BD'],
                    USER_BD=os.environ['USER_BD'],
                    PASS_BD=os.environ['PASS_BD'],
                    NAME_BD=os.environ['NAME_BD'],
                    TOKENBOT=os.environ['TOKENBOT']
                   ):
        run('sudo supervisorctl start botdietas')

def Recargar():
    run("sudo supervisorctl reload")


def Detener():
    run ('sudo supervisorctl stop botdietas')

def Borrado():
    run ('sudo rm -rf DietasBot')

def Test():
    with shell_env(HOST_BD=os.environ['HOST_BD'],
                    USER_BD=os.environ['USER_BD'],
                    PASS_BD=os.environ['PASS_BD'],
                    NAME_BD=os.environ['NAME_BD'],
                    TOKENBOT=os.environ['TOKENBOT']
                   ):
        run('cd DietasBot/botDietas && python test_bot.py')
~~~

* **Configuración interna**.
~~~
[program: botdietas]
autostart=false
command=python bot_dietas.py
user=vagrant
directory=/home/vagrant/DietasBot/botDietas
environment=
  TOKENBOT="{{TOKENBOT}}",
  USER_BD="{{USER_BD}}",
  PASS_BD="{{PASS_BD}}",
  HOST_BD="{{HOST_BD}}",
  NAME_BD="{{NAME_BD}}",
redirect_stderr=true
stdout_logfile=/var/log/supervisor/bot.log
stderr_logfile=/var/log/supervisor/bot-error.log
~~~

Queda definido de esta manera cómo haremos los test de nuestra aplicación, cómo desplegaremos nuestra aplicación y cómo lanzaremos la ejecución del bot.

La ejecución de esta herramienta se basa en el siguiente comando:

~~~
fab -H user@IP-maquina método
~~~

Es por eso que una ejecución en nuestra máquina de los test creados en hitos anteriores queda de la siguiente forma:

![Test fab](http://i345.photobucket.com/albums/p391/maribhez/fabrictest_zpsszcl6jnr.png "Test fab")


Tras esto, y para automatizar todo el proceso he creado tanto un archivo *makefile* como un *script* para el despliegue.

Las órdenes del Makefile creado son las siguientes:

* **despliegue**: Acción de desplegar y aprovisionar nuestra máquina.
* **install**: Similar a la accion anterior.
* **ejecutar**: Acción de lanzar la ejecución del bot.
* **recargar**: Acción de recargar el supervisor configurado.
* **borrar**: Acción de borrar la carpeta creada al clonar este repositorio en la máquina de Azure.
* **test**: Acción de realizar los tests para comprobar el correcto funcionamiento de nuestra máquina.


Por último, el script sólo dispone del siguiente contenido:
~~~
#!/bin/bash

#Instalamos todo lo necesario y lanzamos la aplicación.
fab -H vagrant@52.233.166.73 Instalar
fab -H vagrant@52.233.166.73 Ejecutar
~~~

El propósito de este script es sólo lanzar el bot, para hacer necesario tan sólo el uso de un comando.
