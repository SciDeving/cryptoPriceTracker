install_python:
	python3 -m venv venv && fish venv/bin/activate.fish
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements.txt
