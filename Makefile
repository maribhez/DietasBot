install:
	apt-get update && apt-get install -y python-dev && &&apt-get install -y python-pip &&	pip install -r requirements.txt


test: cd botDietas && python -m unittest test

ejecutar: cd botDietas && python bot_dietas.py
