# BOT DE TELEGRAM PARA EL APOYO DE DIETAS ALIMENTICIAS.

<!-- ![Sin titulo](https://travis-ci.org/maribhez/Infraestructura-Virtual-2016-2017.svg?branch=master) -->

[![Build Status](https://travis-ci.org/maribhez/DietasBot.svg?branch=master)](https://travis-ci.org/maribhez/DietasBot)


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
