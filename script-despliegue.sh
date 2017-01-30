#!/bin/bash

#Instalamos todo lo necesario y lanzamos la aplicación.
fab -H vagrant@52.233.166.73 Instalar
fab -H vagrant@52.233.166.73 Ejecutar
