.PHONY: tests install tests-allure allure-serve

tests:
	.venv/bin/pytest tests/ -v

tests-allure:
	.venv/bin/pytest --alluredir=./allure-results ./tests

allure-serve:
	allure serve ./allure-results

install:
	pip install -r requirements.txt
