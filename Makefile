install:
	@poetry install

lint:
	poetry run flake8 generate_diff

test:
	poetry run pytest -v generate_diff tests/

.PHONY: lint test lint
