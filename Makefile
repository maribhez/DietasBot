despliegue:
	vagrant up --provider=azure
	vagrant provision

install:
	fab -H vagrant@52.233.166.73 Instalar

ejecutar:
	fab -H 	vagrant@52.233.166.73 ejecutar

recargar:
	fab -H 	vagrant@52.233.166.73 Recargar

borrar:
	fab -H 	vagrant@52.233.166.73 Borrado

test:
	fab -H 	vagrant@52.233.166.73 Test
	 
