.PHONY: install test lint

install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run black --check .
	poetry run isort --check .
	poetry run ruff
