install:
	pip install -r requirements.txt


test:
		cd botDietas && pytest

ejecutar:
	cd botDietas && python bot_dietas.py
