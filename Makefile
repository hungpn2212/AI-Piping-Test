build:
	docker compose build

up:
	docker compose up --build

clean_pycache:
	find ./ -name __pycache__ | xargs rm -rf

test:
	pytest .

test-cov:
	pytest . --cov=. --cov-report term-missing

virtualenv:
	python3 -m venv venv

install:
	pip install -r requirements.txt

run:
	uvicorn app.main:app --host 127.0.0.1 --port 3000

run-reload:
	uvicorn app.main:app --host 127.0.0.1 --port 3000 --reload
