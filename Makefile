despliegue:
	vagrant up --provider=azure
	vagrant provision

install:
	fab -H vagrant@52.233.166.73 Instala

ejecutar:
	fab -H 	vagrant@52.233.166.73 Ejecutar

recargar:
	fab -H 	vagrant@52.233.166.73 Recargar

borrar:
	fab -H 	vagrant@52.233.166.73 Borrado

test:
	fab -H 	vagrant@52.233.166.73 Test
