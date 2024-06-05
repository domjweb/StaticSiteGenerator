#!/bin/bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"  # Get the absolute path to the directory containing this script
SRC_DIR="$DIR/src"

if [ -d "$SRC_DIR" ]; then  # Check if src directory exists
    python -m unittest discover -s "$SRC_DIR"
else
    echo "Error: src directory not found!"
    exit 1
fi

