#!/usr/bin/env bash
set -ex
export PIPENV_VERBOSITY=-1

pipenv run mypy --ignore-missing-imports --strict-optional --check-untyped-defs test cafe
pipenv run pytest test -vv