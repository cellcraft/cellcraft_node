#!/bin/bash

set -e

python3.6 -m venv .venv
source .venv/bin/activate

pip install numpy==1.12.1
pip install scipy==0.19.0

source .venv/bin/activate

pip install -r requirements.txt
