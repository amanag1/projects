#!/usr/bin/env sh
set -eu
python -m pip install -e .
knowledge-assistant --folder ./sample_data --question "What is the approval process?"
