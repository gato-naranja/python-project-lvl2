install:
	@poetry install

lint:
	poetry run flake8 generate_diff

.PHONY: lint install test
