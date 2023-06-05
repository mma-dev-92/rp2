#!/bin/bash

PYTHON_PATH=python3
$PYTHON_PATH -m venv venv
source venv/bin/activate
pip install -r requirements.txt
