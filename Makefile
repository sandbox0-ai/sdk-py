.PHONY: apispec build check typecheck check-dist publish-test publish set-version release clean

# Version for publishing (usage: make publish v=0.0.0)
v ?=

set-version:
ifndef v
	@echo "Error: version not specified. Usage: make set-version v=0.0.0"
	@exit 1
endif
	@echo "Setting version to $(v)"
	@sed -i.bak 's/^version = ".*"/version = "$(v)"/' pyproject.toml && rm -f pyproject.toml.bak
	@echo "Version updated to $(v) in pyproject.toml"

# Generate typed low-level SDK code from OpenAPI spec.
apispec:
	@printf "Generating Python API spec code...\n"
	@python3 -m openapi_python_client --version >/dev/null 2>&1 || \
		python3 -m pip install --user openapi-python-client
	@python3 -m openapi_python_client generate \
		--path openapi.yaml \
		--meta none \
		--overwrite \
		--output-path sandbox0/apispec

build: clean
	@python3 -m pip install --user build twine >/dev/null
	@python3 -m build

check:
	@python3 -m compileall -q sandbox0 examples tests
	@python3 -m unittest discover -s tests -p "test_*.py"
	@$(MAKE) typecheck

typecheck:
	@python3 -m pip install --user mypy >/dev/null
	@python3 -m mypy --ignore-missing-imports --follow-imports=skip \
		sandbox0/client.py \
		sandbox0/sandbox.py \
		sandbox0/response.py \
		sandbox0/response_normalize.py

check-dist: build
	@python3 -m twine check dist/*

publish-test: check-dist
ifndef PYPI_TOKEN
	@echo "Error: PYPI_TOKEN not set. Get your token from https://pypi.org/manage/account/token/"
	@exit 1
endif
	@python3 -m twine upload --repository testpypi \
		--username __token__ --password "$(PYPI_TOKEN)" dist/*

publish: check-dist
ifndef PYPI_TOKEN
	@echo "Error: PYPI_TOKEN not set. Get your token from https://pypi.org/manage/account/token/"
	@exit 1
endif
	@python3 -m twine upload \
		--username __token__ --password "$(PYPI_TOKEN)" dist/*

release: set-version publish
	@echo "Released version $(v) successfully!"

clean:
	@rm -rf build dist *.egg-info
