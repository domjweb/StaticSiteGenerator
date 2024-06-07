#!/bin/bash
cd "$(dirname "$0")"

python src/main.py
python -m http.server --directory public 8888

