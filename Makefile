run-format:
	flake8 . --exclude=.venv,__init__.py

update-requirements-file:
	poetry export -f requirements.txt --output requirements.txt --without-hashes