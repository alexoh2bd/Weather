#!/bin/bash

python -m venv venv 
source activate venv
pip install -r requirements.txt

touch .env