# Release Guide

This document describes how to release sandbox0 Python SDK to PyPI.

## Prerequisites

1. PyPI account with 2FA enabled
2. API token from [PyPI Manage Account](https://pypi.org/manage/account/token/)
3. Maintainer or Owner permissions on the `sandbox0` package

## Environment Setup

```bash
export PYPI_NAME="__token__"
export PYPI_TOKEN="pypi-xxx..."  # Your API token from PyPI
```

## Release Process

### 1. Ensure tests pass

```bash
make check
```

### 2. Release to PyPI

```bash
make release v=X.Y.Z
```

This command will:
1. Update the version in `pyproject.toml`
2. Build the distribution packages
3. Upload to PyPI

### 3. Verify the release

Visit https://pypi.org/project/sandbox0/ to confirm the new version is published.

## Testing with TestPyPI (Optional)

Before releasing to PyPI, you can test the package on TestPyPI:

```bash
make publish-test v=X.Y.Z
```

Then install and test:

```bash
pip install --index-url https://test.pypi.org/simple/ sandbox0==X.Y.Z
```

## Available Make Targets

| Target | Description |
|--------|-------------|
| `make set-version v=X.Y.Z` | Update version in pyproject.toml |
| `make build` | Build distribution packages |
| `make check-dist` | Build and validate packages |
| `make publish` | Upload to PyPI (requires PYPI_TOKEN) |
| `make publish-test` | Upload to TestPyPI (requires PYPI_TOKEN) |
| `make release v=X.Y.Z` | Set version and publish to PyPI |
| `make clean` | Remove build artifacts |

## Versioning

This project follows [Semantic Versioning](https://semver.org/):

- **MAJOR**: Incompatible API changes
- **MINOR**: Backward-compatible new features
- **PATCH**: Backward-compatible bug fixes
