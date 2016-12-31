# BOT DE TELEGRAM PARA EL APOYO DE DIETAS ALIMENTICIAS.

<!-- ![Sin titulo](https://travis-ci.org/maribhez/Infraestructura-Virtual-2016-2017.svg?branch=master) -->

[![Build Status](https://travis-ci.org/maribhez/DietasBot.svg?branch=master)](https://travis-ci.org/maribhez/DietasBot)
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

> docker run -e "DATABASE_URL=XXX" -e "HOST_BD=XXXX" -e "NAME_BD=XXXX" -e "PW_BD=XXXX" -e "TOKENBOT=XXXX" -e "USER_BD=XXXX" -i -t contenedoractividadesugrbot /bin/bash

Los parámetros a usar son aquellas credenciales correspodientes a la base de datos de Heroku que habíamos usado en anteriores configuraciones y la del bot que estamos desarrollando. Si todo ha funcionado de la forma esperada podremos pasar a la configuración de Docker sobre Docker Hub. 


* El siguiente paso es sincronizar nuestra cuenta de *Git Hub* con la cuenta ya creada de *Docker Hub* y crear un repositorio. 

![Repositorio](http://i345.photobucket.com/albums/p391/maribhez/Captura2_zps8iaqjx8n.png "Repositorio")

* Tras esto, uan vez que hemos hecho *push* del archivo *Dockerfile* a nuestro repositorio de Git Hub y éste se encuentra actualizado  el repositorio de *Docker Hub* empieza su "Construcción" y se comprueba su correcta funcionamiento. 

![Construcción](http://i345.photobucket.com/albums/p391/maribhez/Captura3_zpsacdyhdv3.png "Construccion")

* Y ya, para descargar, no hay más que usar **docker pull mmaribanhez/botdietas**, siendo esta información que podemos sacar del propio repositorio. 
 ![Descarga](http://i345.photobucket.com/albums/p391/maribhez/Captura4_zps4x77hhre.png "Descarga")

Vemos aquí cómo aparece nuestra descarga en los repositorios de nuestro sistema. 

![Comprobación](http://i345.photobucket.com/albums/p391/maribhez/Captura5_zpsmxial3za.png "Comprobacion")










