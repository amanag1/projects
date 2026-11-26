#!/bin/sh
set -eu
python -m compileall -q src tests
pytest -q
