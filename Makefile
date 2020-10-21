install:
	@poetry install

lint:
	poetry run flake8 generate_diff

test:
	poetry run pytest -q --cov=generate_diff --cov-report xml tests/

.PHONY: lint test lint
