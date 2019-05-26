#!/usr/bin/env bash
set -ex

pipenv run pytest test
pipenv run mypy --ignore-missing-imports --strict-optional --check-untyped-defs test cafe