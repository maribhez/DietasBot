# BOT DE TELEGRAM PARA EL APOYO DE DIETAS ALIMENTICIAS.

<!-- ![Sin titulo](https://travis-ci.org/maribhez/Infraestructura-Virtual-2016-2017.svg?branch=master) -->

[![Build Status](https://travis-ci.org/maribhez/Infraestructura-Virtual-2016-2017.svg?branch=master)](https://travis-ci.org/maribhez/Infraestructura-Virtual-2016-2017)


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
