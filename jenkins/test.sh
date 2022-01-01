#!/bin/bash

echo "test stage"

# creating virtual env
python3 -m venv venv
source venv/bin/activate

# pip3 install, requirements.txt
pip3 install -r requirements.txt

mkdir testreports

# run pytest

python3 -m pytest --cov=application --cov-report term-missing \
    --cov-report xml:testreports/coverage.xml junitxml=testreports/junit_report.xml

# removing venv
deactivate
rm -rf venv