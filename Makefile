.PHONY: apispec build check typecheck check-dist publish-test publish clean

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

build:
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
	@python3 -m twine upload --repository testpypi dist/*

publish: check-dist
	@python3 -m twine upload dist/*

clean:
	@rm -rf build dist *.egg-info
