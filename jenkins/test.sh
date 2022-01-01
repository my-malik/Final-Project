#!/bin/bash

echo "test stage"

# creating virtual env
python3 -m venv venv
source venv/bin/activate

# pip3 install, requirements.txt
pip3 install -r requirements.txt



# run pytest

python3 -m pytest

# removing venv
deactivate
rm -rf venv