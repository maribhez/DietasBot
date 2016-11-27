install:
	pip install -r requirements.txt


test:
		cd botDietas && py.test

ejecutar:
	cd botDietas && python bot_dietas.py
