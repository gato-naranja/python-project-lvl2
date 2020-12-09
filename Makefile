install:
	@poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -q --cov=gendiff --cov-report xml tests/

.PHONY: lint test lint
